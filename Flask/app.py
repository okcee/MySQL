import os

from configparser import ConfigParser
from flask import Flask, render_template, request, redirect, url_for
from cliente import Cliente
from cliente_forma import ClienteForma
from cliente_dao import ClienteDAO

app = Flask(__name__)

# --- Cargar configuración de datos sensibles ---
config = ConfigParser() # Llama al módulo de seguridad. Cargar configuración desde .config.ini ---

config_path = os.path.join(os.path.dirname(__file__), '.config.ini') # __file__ se refiere al archivo actual (app.py)
# os.path.dirname obtiene el directorio de ese archivo
# os.path.join une el directorio con el nombre del archivo .ini

if not os.path.exists(config_path):
    raise RuntimeError(f"El archivo de configuración no se encontró en: {config_path}")
config.read(config_path)

# Asigna la SECRET_KEY leída del archivo .ini a la configuración de Flask
try:
    app.config['SECRET_KEY'] = config.get('FlaskSettings', 'SECRET_KEY')
except Exception as e:
    raise RuntimeError(f"Error al leer SECRET_KEY desde .config.ini: {e}")

# --- Fin de la carga de configuración  de datos sensibles ---

titulo_app = 'Zona Fit (GYM)'

@app.route('/')  # url: http://localhost:5000/
@app.route('/index.html') # url: http://localhost:5000/index.html

def inicio():
    app.logger.debug('Entramos al path de inicio /')
    # Recuperamos los clientes de la base de datos
    clientes_db = ClienteDAO.seleccionar()
    # Creamos un objeto de formulario vacío
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

# --- NUEVA RUTA PARA GUARDAR ---
@app.route('/guardar', methods=['POST'])
def guardar():
    app.logger.debug(f'Entrando a /guardar con método {request.method}')
    # 1. Creamos una instancia del formulario y la poblamos con los datos recibidos
    forma = ClienteForma(request.form)
    app.logger.debug(f'Datos recibidos en el form: {request.form}')

    # 2. Validamos el formulario usando WTForms
    if forma.validate_on_submit():
        app.logger.info('Formulario válido. Procesando inserción...')
        # 3. Creamos un objeto Cliente con los datos validados del formulario
        cliente_nuevo = Cliente(
            nombre=forma.nombre.data,
            apellido=forma.apellido.data,
            membresia=forma.membresia.data
        )
        # 4. Usamos el DAO para insertar el nuevo cliente
        registros_insertados = ClienteDAO.insertar(cliente_nuevo)
        app.logger.info(f'Cliente insertado: {cliente_nuevo}, Registros afectados: {registros_insertados}')
        # 5. Redirigimos al usuario a la página de inicio (PRG Pattern)
        return redirect(url_for('inicio'))
    else:
        # 6. Si la validación falla:
        app.logger.warning(f'Validación fallida: {forma.errors}')
        # Idealmente, volverías a renderizar el index mostrando los errores.
        # Por simplicidad aquí, solo redirigimos a inicio.
        # Para mostrar errores, harías algo como:
        # clientes_db = ClienteDAO.seleccionar()
        # return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=forma)
        return redirect(url_for('inicio')) # Redirección simple por ahora
# --- FIN NUEVA RUTA ---

if __name__ == '__main__':
    app.run(debug=True)