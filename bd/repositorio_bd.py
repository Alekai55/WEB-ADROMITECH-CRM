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


def actualizar_lead(id_lead, nombre, empresa, telefono, email, fuente_captacion, estado, fecha_contacto):
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
        valores = (nombre, empresa, telefono, email, fuente_captacion, estado, fecha_contacto, id_lead)
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
