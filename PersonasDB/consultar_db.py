'''Ejemplo de uso de SELECT con archivo de seguridad de credenciales'''

import configparser
import mysql.connector
import os  # Aunque no es estrictamente necesario aquí, a menudo es útil

# Crear un objeto ConfigParser
config = configparser.ConfigParser()

try:
    # Leer el archivo de configuración
    config.read('.config.ini')  # Usamos .config.ini ahora

    # Obtener los datos de la sección 'database'
    db_config = {
        "host": config['database']['host'],
        "user": config['database']['user'],
        "password": config['database']['password'],
        "database": config['database']['database']
    }

    # Establecer la conexión a la base de datos
    conexion = mysql.connector.connect(**db_config)
    cursor = conexion.cursor()

    # Sentencia SELECT que quieres ejecutar (¡Reemplaza con tu consulta real!)
    query = "SELECT * FROM tu_tabla"  # Reemplaza "tu_tabla" con el nombre de tu tabla

    # Ejecutar la consulta
    cursor.execute(query)

    # Obtener todos los resultados
    resultados = cursor.fetchall()

    # Imprimir los resultados
    for fila in resultados:
        print(fila)

    # También puedes obtener los nombres de las columnas (opcional)
    nombres_columnas = [column[0] for column in cursor.description]
    print("\nNombres de las columnas:", nombres_columnas)

except configparser.NoSectionError:
    print("Error: La sección 'database' no se encontró en el archivo de configuración.")
except configparser.NoOptionError as e:
    print(f"Error: La clave '{e.option}' no se encontró en la sección 'database'.")
except mysql.connector.Error as err:
    print(f"Error al conectar o ejecutar la consulta: {err}")
except FileNotFoundError:
    print("Error: El archivo '.config.ini' no se encontró.")
finally:
    # Cerrar el cursor y la conexión
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conexion' in locals() and conexion and conexion.is_connected():
        conexion.close()
        print("Conexión a MySQL cerrada.")