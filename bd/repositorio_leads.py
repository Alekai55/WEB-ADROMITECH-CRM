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
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()
