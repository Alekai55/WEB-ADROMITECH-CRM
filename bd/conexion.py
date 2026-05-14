import mysql.connector
from mysql.connector import Error


def crear_conexion():
    """Conexión con nuestra base de datos real alojada en Clever Cloud, en un principio
    planteamos hacerla con una base de datos local inventada, pero de esta forma, hemos logrado
    trabajar todos simultáneamente en las aplicaciones
    """
    try:
        conexion = mysql.connector.connect(
            host="b6vqc2uyeo3cmbs6cgrx-mysql.services.clever-cloud.com",
            user="ufigwhllqfa0jdm0",
            password="IhmnVOXgPNuWuKFBEzYm",
            database="b6vqc2uyeo3cmbs6cgrx",
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
