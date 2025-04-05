# Elimina o borra un registro existente de una base de datos MySQL

'''Paso1: Importar módulos'''
import mysql.connector
import configparser
import os

'''Paso2: Crear un objeto config que llame a la clase ConfigParser'''
config = configparser.ConfigParser()
conexion = None  # Initialize conexion to None
cursor = None  # Initialize cursor to None

try:
    '''Paso3: Leer el archivo de configuración'''
    config.read('.config.ini')
    
    '''Paso4: Obtener los datos de la sección `database` '''
    db_config = {
        "host": config['database']['host'],  # IP 127.0.0.1
        "user": config['database']['user'],
        "password": config['database']['password'],
        "database": config['database']['database']
    }

    '''Paso5: Establecer la Conexión'''
    conexion = mysql.connector.connect(**db_config)
    '''Paso6: Crear un Cursor'''
    cursor = conexion.cursor()

    '''Paso7: Ejecutar la Sentencia DELETE'''
    query = "DELETE FROM personas WHERE id=%s"
    valores = (7,)

    # Ejecutar la consulta
    cursor.execute(query, valores)
    conexion.commit() # guarda los cambios en la base de datos
    # Obtener todos los resultados
    print(f'Se ha eliminado la información del registro en la base de datos del ID: {valores}')

# Paso8: Capturar excepciones
except Exception as e:
    print(f"An unexpected error occurred: {e}")
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
    if cursor:
        cursor.close()
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión a MySQL cerrada.")
