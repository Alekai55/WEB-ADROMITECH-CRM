from bd.conexion import crear_conexion


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
