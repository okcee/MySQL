''' Patrón de diseño DAO
DAO = Data Accesss Object
Este patrón se utiliza para acceder a la información de una entidad de nuestra aplicación.
En este caso a través del cliente DAO vamos a acceder a la información de la tabla cliente y poder mediante métodos de la clase Cliente DAO, interactuar con la clase Cliente para ejecutar sentencias en la tabla cliente
Esta forma de relacionar los datos es el principio de aplicaciones que se conocen como ORM (Object Relational Mappin), o también de mapeo relación entidad
'''

import sys  # Importa el módulo 'sys' para acceder a funcionalidades del sistema, como la ruta de búsqueda de módulos.
import os  # Importa el módulo 'os' para interactuar con el sistema operativo, como la manipulación de rutas de archivos.

from conexion import Conexion  # Importa la clase 'Conexion' desde el módulo 'conexion.py' (ahora accesible gracias a la modificación de sys.path).
from cliente import Cliente  # Importa la clase 'Cliente' desde el módulo 'cliente.py' (ahora accesible gracias a la modificación de sys.path).

class ClienteDAO:  # Define la clase 'clienteDAO' que implementa el patrón DAO para la entidad 'cliente'.
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'  # Define una constante con la consulta SQL para seleccionar todos los registros de la tabla 'cliente' ordenados por 'id'.
    INSERTAR = 'INSERT INTO cliente (nombre, apellido, membresia) VALUES (%s, %s, %s)'  # Define una constante con la consulta SQL para insertar un nuevo registro en la tabla 'cliente'.
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'  # Define una constante con la consulta SQL para actualizar un registro existente en la tabla 'cliente'.
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'  # Define una constante con la consulta SQL para eliminar un registro de la tabla 'cliente' por su 'id'.
    
    @classmethod  # Define un método de clase, que se puede llamar directamente en la clase sin necesidad de instanciar un objeto.
    def seleccionar(cls):  # Define el método 'seleccionar' para obtener todos los clientes de la base de datos.
        conexion = None  # Inicializa la variable 'conexion' a 'None' para almacenar la conexión a la base de datos.
        try:  # Inicia un bloque 'try' para manejar posibles excepciones.
            conexion = Conexion.obtener_conexion()  # Obtiene una conexión a la base de datos utilizando el método 'obtener_conexion' de la clase 'Conexion'.
            cursor = conexion.cursor()  # Crea un objeto cursor para ejecutar consultas SQL.
            cursor.execute(cls.SELECCIONAR)  # Ejecuta la consulta SQL definida en la constante 'SELECCIONAR'.
            registros = cursor.fetchall()  # Obtiene todos los registros resultantes de la consulta y los almacena en 'registros'.
            # Mapeo de clase-tabla cliente
            clientes = []  # Inicializa una lista vacía llamada 'clientes' para almacenar los objetos 'Cliente'.
            for registro in registros:  # Itera sobre cada registro obtenido de la base de datos.
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])  # Crea un objeto 'Cliente' con los datos del registro.
                clientes.append(cliente)  # Añade el objeto 'Cliente' a la lista 'clientes'.
            return clientes  # Retorna la lista de objetos 'Cliente'.
        except Exception as e:  # Captura cualquier excepción que ocurra dentro del bloque 'try'.
            print(f'Ocurrió un error al seleccionar los clientes: {e}')  # Imprime un mensaje de error con la excepción capturada.
        finally:  # Bloque 'finally' que se ejecuta siempre, haya o no excepciones.
            if conexion is not None:  # Verifica si la variable 'conexion' tiene una conexión.
                cursor.close()  # Cierra el cursor.
                Conexion.liberar_conexion(conexion)  # Libera la conexión a la base de datos utilizando el método 'liberar_conexion' de la clase 'Conexion'.

    @classmethod
    def insertar(cls, cliente):
        conexion = None # Inicializa la variable 'conexion' a 'None' para almacenar la conexión a la base de datos.
        try: # Inicia un bloque 'try' para manejar posibles excepciones.
            conexion = Conexion.obtener_conexion() # Obtiene una conexión a la base de datos utilizando el método 'obtener_conexion' de la clase 'Conexion'.
            cursor = conexion.cursor() # Crea un objeto cursor para ejecutar consultas SQL.
            valores = (cliente.nombre, cliente.apellido, cliente.membresia) # Especifica los valores para hacer el INSERT, tomando los valores del objeto cliente
            cursor.execute(cls.INSERTAR, valores) # Ejecuta la consulta SQL definida en el atributo constante 'INSERTAR'.
            conexion.commit() # Confirma la subida los cambios en la base de datos.
            return cursor.rowcount # Está variable indica cuatos datos se modificaron en la base de datos
        except Exception as e:
            print(f'Ocurrió un error al insertar el cliente: {e}')
        finally:  # Bloque 'finally' que se ejecuta siempre, haya o no excepciones.
            if conexion is not None:  # Verifica si la variable 'conexion' tiene una conexión.
                cursor.close()  # Cierra el cursor.
                Conexion.liberar_conexion(conexion)  # Libera la conexión a la base de datos utilizando el método 'liberar_conexion' de la clase 'Conexion'.
    
    @classmethod
    def actualizar(cls, cliente): # Aquí el objeto cliente, a diferencia de los anteriores, debería de tener valor de id
        conexion = None
        try: # Inicia un bloque 'try' para manejar posibles excepciones.
            conexion = Conexion.obtener_conexion() # Obtiene una conexión a la base de datos utilizando el método 'obtener_conexion' de la clase 'Conexion'.
            cursor = conexion.cursor() # Crea un objeto cursor para ejecutar consultas SQL.
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id) # Especifica los valores para hacer el UPDATE, tomando los valores del objeto cliente
            cursor.execute(cls.ACTUALIZAR, valores) # Ejecuta la consulta SQL definida en el atributo constante 'ACTUALIZAR'.
            conexion.commit() # Confirma la subida los cambios en la base de datos.
            return cursor.rowcount # Está variable indica cuatos datos se modificaron en la base de datos
        except Exception as e:
            print(f'Ocurrió un error al insertar el cliente: {e}')
        finally:  # Bloque 'finally' que se ejecuta siempre, haya o no excepciones.
            if conexion is not None:  # Verifica si la variable 'conexion' tiene una conexión.
                cursor.close()  # Cierra el cursor.
                Conexion.liberar_conexion(conexion)  # Libera la conexión a la base de datos utilizando el método 'liberar_conexion' de la clase 'Conexion'.
    
    @classmethod
    def eliminar(cls, cliente): # basta con el valor de id para eliminar el registro de tipo cliente
        conexion = None
        try: # Inicia un bloque 'try' para manejar posibles excepciones.
            conexion = Conexion.obtener_conexion() # Obtiene una conexión a la base de datos utilizando el método 'obtener_conexion' de la clase 'Conexion'.
            cursor = conexion.cursor() # Crea un objeto cursor para ejecutar consultas SQL.
            valores = (cliente.id,) # Especifica el valor de "ID" para ejecutar la sentencia delete, tomando los valores del objeto cliente (como valores es una tupla, añadimos la "," después del primer valor para especificar que es una tupla con solo un dato)
            cursor.execute(cls.ELIMINAR, valores) # Ejecuta la consulta SQL definida en el atributo constante 'ELIMINAR'.
            conexion.commit() # Confirma la subida del cambio en la base de datos.
            return cursor.rowcount # Está variable indica cuatos datos se modificaron en la base de datos
        except Exception as e:
            print(f'Ocurrió un error al insertar el cliente: {e}')
        finally:  # Bloque 'finally' que se ejecuta siempre, haya o no excepciones.
            if conexion is not None:  # Verifica si la variable 'conexion' tiene una conexión.
                cursor.close()  # Cierra el cursor.
                Conexion.liberar_conexion(conexion)  # Libera la conexión a la base de datos utilizando el método 'liberar_conexion' de la clase 'Conexion'.


# TESTING FILE
if __name__ == '__main__':  # Verifica si el script se está ejecutando directamente (no importado como módulo).
    
    # Insertar cliente
    # cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia='300')
    # clientes_insertados = clienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')
    
    # Actualizar cliente
    # cliente_actualizar = Cliente (3, 'Alexa', 'Tellez', '400')
    # clientes_actualizados = clienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados: {clientes_actualizados}')
    
    # Eliminar cliente
    # cliente_eliminar = Cliente(id=3)
    # clientes_eliminados = clienteDAO.eliminar(cliente_eliminar)
    # print(f'Clientes eliminados: {clientes_eliminados}')
    
    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()  # Llama al método 'seleccionar' de la clase 'clienteDAO' para obtener todos los clientes.
    for cliente in clientes:  # Itera sobre la lista de clientes obtenida.
        print(cliente)  # Imprime la información de cada cliente (utilizando el método '__str__' de la clase 'Cliente').
    
