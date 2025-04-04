'''Paso1:
Importar el Módulo'''
import mysql.connector

'''Paso1:
Establecer la Conexión'''
db_config = {
    "host": "localhost", # IP 127.0.0.1
    "user": "root",
    "password": "tu_contraseña",
    "database": "personas_db"
}

try:
    conexion = mysql.connector.connect(**db_config)
    # ... (resto del código)
except mysql.connector.Error as err:
    print(f"Error al conectar: {err}")

'''Paso 3:
Crear un Cursor'''



'''Paso4:
Ejecutar la Consulta SELECT'''

