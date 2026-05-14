from flask import Flask, render_template, request, redirect, url_for, jsonify
from bd.repositorio_bd import obtener_leads, insertar_lead, actualizar_lead

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/leads")
def leads():
    lista_leads = obtener_leads()
    return jsonify(lista_leads)


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


if __name__ == "__main__":
    app.run(debug=True, port=5005)
