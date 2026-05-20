from bd.conexion import crear_conexion


def contar_registros(
    tabla,
):  # funcion para contar registros de cualquier tabla de la base de datos
    """Devuelve el total de filas de una tabla. Devuelve 0 si falla o la tabla no existe."""
    conexion = crear_conexion()
    if conexion is None:
        return 0
    try:
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT COUNT(*) FROM `{tabla}`"
        )  # ejecución de la consulta para cualquier tabla, las `` sirven para evitar errores de nombres
        resultado = (
            cursor.fetchone()
        )  # esto sirve para traer solo una fila (es decir cuenta el numero de registros de la tabla y lo devuelve como número)
        return resultado[0] if resultado else 0
    except Exception:
        return 0
    finally:
        # El bloque finally SIEMPRE se ejecuta al final (haya habido error o no) para limpiar recursos.
        if "cursor" in locals() and cursor is not None:
            # Comprobamos que el cursor se creó para evitar errores al cerrarlo. Si existe, lo cerramos.
            cursor.close()
        if conexion is not None and conexion.is_connected():
            # Comprobamos que la conexión existe y sigue abierta. Si es así, la cerramos para no colapsar la BD.
            conexion.close()


def obtener_leads():
    conexion = crear_conexion()
    if conexion is None:
        return []

    try:
        cursor = conexion.cursor(dictionary=True)
        # Hacemos la consulta a la tabla 'leads'
        cursor.execute("SELECT * FROM leads")
        leads = cursor.fetchall()
        return leads
    except Exception as e:
        print(f"Error al obtener leads: {e}")
        return []
    finally:
        if "cursor" in locals() and cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()


# MÉTODO para que la web interprete el lenguaje sql y tome los datos de la tabla leads para insertar los nuevos correctamente
def insertar_lead(
    nombre, empresa, telefono, email, fuente_captacion, estado, fecha_contacto
):
    """Inserta un nuevo lead en la base de datos."""
    conexion = crear_conexion()
    if conexion is None:
        return False

    try:
        cursor = conexion.cursor()
        sql = """
            INSERT INTO leads (nombre, empresa, telefono, email, fuente_captacion, estado, fecha_contacto)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            nombre,
            empresa,
            telefono,
            email,
            fuente_captacion,
            estado,
            fecha_contacto,
        )
        cursor.execute(sql, valores)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al insertar lead: {e}")
        return False
    finally:
        if "cursor" in locals() and cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()


# MÉTODO para que permita realizar un update a los datos de la tabla leads
def actualizar_lead(
    id_lead, nombre, empresa, telefono, email, fuente_captacion, estado, fecha_contacto
):
    """Actualiza los datos de un lead existente por su id."""
    conexion = crear_conexion()
    if conexion is None:
        return False

    try:
        cursor = conexion.cursor()
        sql = """
            UPDATE leads
            SET nombre = %s, empresa = %s, telefono = %s, email = %s,
                fuente_captacion = %s, estado = %s, fecha_contacto = %s
            WHERE id_lead = %s
        """
        valores = (
            nombre,
            empresa,
            telefono,
            email,
            fuente_captacion,
            estado,
            fecha_contacto,
            id_lead,
        )
        cursor.execute(sql, valores)
        conexion.commit()
        return cursor.rowcount > 0  # True si se actualizó al menos 1 fila
    except Exception as e:
        print(f"Error al actualizar lead: {e}")
        return False
    finally:
        if "cursor" in locals() and cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()


# MÉTODO para interpretar el delete y así poder borrar los datos de un lead
def eliminar_lead(id_lead):
    """Elimina un lead de la base de datos por su id."""
    conexion = crear_conexion()
    if conexion is None:
        return False

    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM leads WHERE id_lead = %s", (id_lead,))
        conexion.commit()
        return cursor.rowcount > 0  # True si se eliminó al menos 1 fila
    except Exception as e:
        print(f"Error al eliminar lead: {e}")
        return False
    finally:
        if "cursor" in locals() and cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()

# MÉTODO para obtener los clientes
def obtener_cliente():
    conexion = crear_conexion()
    if conexion is None:
        return []

    try:
        cursor = conexion.cursor(dictionary=True)
        # Hacemos la consulta a la tabla 'cliente'
        cursor.execute("SELECT * FROM cliente")
        leads = cursor.fetchall()
        return leads
    except Exception as e:
        print(f"Error al obtener clientes: {e}")
        return []
    finally:
        if "cursor" in locals() and cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()
# MÉTODO para obtener los comerciales
def obtener_comercial():
    conexion = crear_conexion()
    if conexion is None:
        return []

    try:
        cursor = conexion.cursor(dictionary=True)
        # Hacemos la consulta a la tabla 'comerciales'
        cursor.execute("SELECT * FROM comercial")
        leads = cursor.fetchall()
        return leads
    except Exception as e:
        print(f"Error al obtener comerciales: {e}")
        return []
    finally:
        if "cursor" in locals() and cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()
 # MÉTODO para obtener los pedidos
def obtener_pedidos():
    conexion = crear_conexion()
    if conexion is None:
        return []

    try:
        cursor = conexion.cursor(dictionary=True)
        # Hacemos la consulta a la tabla 'pedido'
        cursor.execute("SELECT * FROM pedido")
        pedidos = cursor.fetchall()
        return pedidos
    except Exception as e:
        print(f"Error al obtener pedidos: {e}")
        return []
    finally:
        if "cursor" in locals() and cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close() 
          
# MÉTODO para obtener las facturas
def obtener_facturas():
    conexion = crear_conexion()
    if conexion is None:
        return []

    try:
        cursor = conexion.cursor(dictionary=True)
        # Hacemos la consulta a la tabla 'factura'
        cursor.execute("SELECT * FROM factura")
        facturas = cursor.fetchall()
        return facturas
    except Exception as e:
        print(f"Error al obtener facturas: {e}")
        return []
    finally:
        if "cursor" in locals() and cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()



