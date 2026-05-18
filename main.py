from flask import Flask, render_template, request, redirect, url_for, jsonify
from bd.repositorio_bd import (
    obtener_leads,
    insertar_lead,
    actualizar_lead,
    eliminar_lead,
    obtener_cliente,
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/admin-leads")
def admin_leads():
    """Renderiza la página de gestión de leads."""
    return render_template("leads.html")

@app.route("/admin-clientes")  
def admin_clientes():
   """Renderiza la página de gestión de clientes."""
   return render_template("clientes.html") 


@app.route("/dashboard/stats")
def dashboard_stats():
    """Devuelve los totales de leads, clientes y pedidos para el dashboard."""
    from bd.repositorio_bd import contar_registros

    return jsonify(
        {
            "leads": contar_registros("leads"),
            "clientes": contar_registros("cliente"),
            "pedidos": contar_registros("pedido"),
        }
    )


@app.route("/leads")
def leads():
    lista_leads = obtener_leads()
    return jsonify(lista_leads)

@app.route("/clientes")
def clientes():
    lista_cliente = obtener_cliente()
    return jsonify(lista_cliente)  



# MÉTODO para que al arrancar la web, sepa leer los datos de la base de datos y permita insertar nuevos
@app.route("/leads/nuevo", methods=["POST"])
def nuevo_lead():
    """Recibe los datos del formulario modal y los inserta en la BD."""
    datos = request.get_json()
    exito = insertar_lead(
        nombre=datos.get("nombre"),
        empresa=datos.get("empresa"),
        telefono=datos.get("telefono"),
        email=datos.get("email"),
        fuente_captacion=datos.get("fuente_captacion"),
        estado=datos.get("estado"),
        fecha_contacto=datos.get("fecha_contacto"),
    )
    if exito:
        return jsonify({"ok": True}), 201
    else:
        return (
            jsonify({"ok": False, "error": "Error al insertar en la base de datos"}),
            500,
        )


# MÉTODO para que al arrancar la web, pueda realizar cambios en la base de datos a través del respectivo botón
@app.route("/leads/editar", methods=["PUT"])
def editar_lead():
    """Recibe los datos actualizados del lead y ejecuta el UPDATE."""
    datos = request.get_json()
    exito = actualizar_lead(
        id_lead=datos.get("id_lead"),
        nombre=datos.get("nombre"),
        empresa=datos.get("empresa"),
        telefono=datos.get("telefono"),
        email=datos.get("email"),
        fuente_captacion=datos.get("fuente_captacion"),
        estado=datos.get("estado"),
        fecha_contacto=datos.get("fecha_contacto"),
    )
    if exito:
        return jsonify({"ok": True}), 200
    else:
        return jsonify({"ok": False, "error": "No se pudo actualizar el lead"}), 500


# MÉTODO para que al arrancar la web, pueda eliminar datos de la base de datos
@app.route("/leads/eliminar/<int:id_lead>", methods=["DELETE"])
def eliminar_lead_route(id_lead):
    """Elimina un lead por su id."""
    exito = eliminar_lead(id_lead)
    if exito:
        return jsonify({"ok": True}), 200
    else:
        return jsonify({"ok": False, "error": "No se pudo eliminar el lead"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5005)
