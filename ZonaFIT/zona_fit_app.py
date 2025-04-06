'''Zona Fit APP'''
import sys  # Importa el módulo 'sys' para acceder a funcionalidades del sistema, como la ruta de búsqueda de módulos.
import os  # Importa el módulo 'os' para interactuar con el sistema operativo, como la manipulación de rutas de archivos.

from cliente import Cliente
from cliente_dao import clienteDAO

print('**** Clientes Zona Fit (GIM) ****')
opcion = None
while opcion != 5:
    print(f"""\nMenu:
        1. Listar clientes
        2. Agregar cliente
        3. Actualizar cliente
        4. Eliminar cliente
        5. Salir""")
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1: # Listar clientes
        clientes = clienteDAO.seleccionar()
        print('\n*** Listado de clientes ***')
        for cliente in clientes:
            print(cliente)
    elif opcion == 2: # Agregar cliente
        nombre_var = input('Ingrese el nombre del cliente: ')
        apellido_var = input('Ingrese el apellido del cliente: ')
        membresia_var = input('Ingrese la membresia del cliente: ')
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_insertados = clienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}')
    elif opcion == 3: # Modificar un cliente
        id_cliente_var = int(input('Ingrese el id del cliente a modificar: '))
        nombre_var = input('Ingrese el nombre del cliente: ')
        apellido_var = input('Ingrese el apellido del cliente: ')
        membresia_var = input('Ingrese la membresia del cliente: ')
        cliente = Cliente(id=id_cliente_var, nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_actualizados = clienteDAO.actualizar(cliente)
        print(f'Clientes actualizados: {clientes_actualizados}')
    elif opcion == 4: # Eliminar un cliente
        id_cliente_var = int(input('Ingrese el id del cliente a eliminar: '))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = clienteDAO.eliminar(cliente)
        print(f'Clientes eliminados: {clientes_eliminados}')
else:
    print("Salimos de la aplicación")

