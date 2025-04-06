'''Clase cliente, también conocida como clase modelo o clase de dominio'''

class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia
    
    def __str__(self): # Para poder imprimir en cualquier momento el estado de este objeto, que son los valores de los atributos de nuestro objeto
        return (f'Id: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Membresia: {self.membresia}')
    