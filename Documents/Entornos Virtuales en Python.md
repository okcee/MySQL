# Introducción a Entornos Virtuales en Python

## ¿Qué son los entornos virtuales?
Espacios aislados en el sistema operativo con dependencias locales para proyectos Python, independientes de las instaladas globalmente. Permiten tener diferentes versiones de librerías para distintos proyectos sin conflictos.

## El Problema sin Entornos Virtuales
Trabajar en múltiples proyectos con diferentes dependencias (ej., distintas versiones de Django) sin entornos virtuales genera problemas de compatibilidad, requiriendo desinstalar e instalar librerías constantemente, y posibles fallos en el entorno del cliente.

## ¿Máquinas Virtuales como Solución?
Aunque las máquinas virtuales aíslan las dependencias, son pesadas, consumen muchos recursos y tienen tiempos de arranque lentos. No es práctico para gestionar solo dependencias de Python.

## La Solución: Entornos Virtuales en Python
Un entorno (eng: **environment**) virtual aísla las dependencias de un proyecto. Python toma las librerías de este espacio aislado en lugar del sistema operativo global. Se pueden tener múltiples entornos aislados.

## Beneficios
- Solucionan problemas de compatibilidad entre proyectos.
- Práctica recomendada (casi obligatoria) en desarrollo Python.
- Cambio rápido entre entornos sin sobrecarga.

# virtualenv: Herramienta para Entornos Python Aislados

Herramienta para crear entornos Python aislados con sus propios directorios de instalación, sin compartir librerías con otros entornos (opcionalmente, tampoco con las globales). Es la forma más fácil y recomendada de configurar entornos Python personalizados.

## Diferencia entre virtualenv y venv
- `venv` viene con Python 3 (no en Python 2).
- `virtualenv` ofrece más funcionalidades que `venv`.
- Se recomienda instalar y usar `virtualenv` en lugar de `venv` con Python 3.
- `venv` es más lento (sin el método de inicialización `app-data`).
- `venv` es menos extensible.
- `venv` no puede crear entornos virtuales para versiones de Python instaladas arbitrariamente (ni descubrirlas automáticamente).
- `venv` no se puede actualizar mediante `pip`.

`virtualenv` resuelve el problema principal, la gestión de dependencias y versiones entre diferentes proyectos Python. Si dos aplicaciones requieren versiones conflictivas de la misma librería, instalar todo globalmente puede generar problemas. También ayuda a mantener un entorno estable para una aplicación específica y a trabajar sin permisos para modificar la instalación global de Python.  

`virtualenv` crea un entorno con sus propios directorios de instalación, sin compartir librerías con otros entornos `virtualenv` (y opcionalmente, sin acceder a las librerías instaladas globalmente).  

## Instalación de Virtualenv
Virtualenv solo se instala en servidores DreamHost para Python 2. Si está trabajando con Python 3, debe instalar virtualenv usando pip3. Para ello, en la consola de comandos:  
Para Python 3, usar `pip3`:
```bash
pip3 install virtualenv
```

Creación de un entorno virtual con una versión personalizada de Python.  
Hay solo otros pocos comandos útiles que deberías conocer (hay más en la documentación de la herramienta), pero estos son los que usarás de forma habitual:  
- deactivate — Salir del entorno virtual Python actual
- workon — Listar los entornos virtuales disponibles
- workon name_of_environment — Activar el entorno virtual Python especificado
- rmvirtualenv name_of_environment — Borrar el entorno especificado.

Por ejemplo, el siguiente comando crea un virtualenv llamado 'venv' y usa el indicador -p para especificar la ruta completa a la versión de Python3 que acaba de instalar. Podemos nombrar el virtualenv como queramos (Ejemplo venv).  
Ejemplos:  
```bash
virtualenv -p /home/username/opt/python-3.10.1/bin/python3 venv

virtualenv -p /home/username/miniconda3/python.exe VirtualLearning

virtualenv -p C:/Users/Okcee/miniconda3/python.exe VirtENV

```
El comando para instalar la última versión de pip es:
```bash
python -m pip install --upgrade pip
```
Comando actualizar:
```bash
pip3 install --upgrade pip
```

# Configurar un entorno virtual tipo "virtualenv" en "vs code" para que sea el entorno virtual por defecto del workspace y, que puede ejecutar un REPL : Entorno interactivo para probar código en tiempo real.

Ese entorno implica los siguientes pasos:  

## 1. Crear y Activar el Entorno Virtual (si aún no lo tienes):

Abre la terminal en la raíz de tu proyecto y ejecuta los siguientes comandos:
```Bash
# Crear el entorno virtual (si no existe)
python -m venv .venv  # Usando el módulo venv (integrado en Python 3)

# virtualenv .venv     # Si prefieres usar virtualenv, debes instalarlo primero:
pip install virtualenv

# Activar el entorno virtual
# En Windows:
.venv\Scripts\activate
# En macOS y Linux:
source .venv/bin/activate
# .venv: Es una convención común para nombrar el directorio del entorno virtual. El punto al inicio lo hace oculto en algunos sistemas.
```

## 2. Seleccionar el Intérprete de Python del Entorno Virtual en VS Code:

VS Code necesita saber qué intérprete de Python usar para tu workspace. Sigue estos pasos:

Abre tu proyecto en VS Code.
Abre la Paleta de Comandos (Ctrl+Shift+P en Windows/Linux, Cmd+Shift+P en macOS).
Escribe y selecciona "Python: Select interpreter".
VS Code mostrará una lista de intérpretes de Python disponibles. Busca la ruta del intérprete python (o python3) que se encuentra dentro de tu directorio .venv. Debería ser algo como:
Windows: .\.venv\Scripts\python.exe
macOS/Linux: ./.venv/bin/python
Selecciona este intérprete.

## 3. Configurar el Entorno Virtual como Predeterminado del Workspace:

Una vez que has seleccionado el intérprete del entorno virtual, VS Code generalmente recordará esta selección para tu workspace. Puedes verificarlo y configurarlo explícitamente en la configuración del workspace:

Ve a "Archivo" > "Preferencias" > "Configuración" (o Ctrl+, / Cmd+,).

En la barra de búsqueda, escribe "Python: Python Path".

En la pestaña "Workspace", asegúrate de que la ruta que aparece en "Python: Python Path" sea la ruta al intérprete de Python dentro de tu directorio .venv (la misma que seleccionaste en el paso anterior).

Si no aparece automáticamente, puedes hacer clic en "Editar en settings.json" (debajo de la configuración) y añadir o modificar la siguiente línea dentro del objeto JSON:

JSON

{
    "python.pythonPath": "./.venv/bin/python" // Para macOS/Linux
    // o
    //"python.pythonPath": ".\\.venv\\Scripts\\python.exe" // Para Windows
}
Guarda el archivo settings.json.

4. Ejecutar un REPL (Entorno Interactivo):

Con el entorno virtual configurado como el intérprete predeterminado del workspace, puedes ejecutar un REPL de Python dentro de VS Code de varias maneras:

Usando la Terminal Integrada:

Abre la Terminal Integrada en VS Code ("Terminal" > "Nuevo Terminal" o Ctrl+`).
Si activaste el entorno virtual en tu shell antes de abrir VS Code, la terminal integrada debería heredar ese entorno. Puedes verificarlo viendo el nombre del entorno virtual entre paréntesis al inicio del prompt (ej., (.venv) tu_usuario@tu_maquina:~/tu_proyecto$).
Si no está activado automáticamente, puedes activarlo manualmente en la terminal integrada usando los comandos source .venv/bin/activate (macOS/Linux) o .venv\Scripts\activate (Windows).
Una vez que el entorno esté activo en la terminal, simplemente escribe python o python3 y presiona Enter para iniciar el REPL.
Usando la Extensión de Python de VS Code (Interactive Window):

Crea un archivo .py en tu workspace (si no tienes uno).
Selecciona algunas líneas de código Python en el archivo.
Haz clic derecho y selecciona "Ejecutar selección/línea en la ventana interactiva de Python".
Esto abrirá una ventana interactiva donde se ejecutará el código seleccionado y te permitirá escribir más código en tiempo real dentro del contexto del entorno virtual configurado.
También puedes simplemente abrir una ventana interactiva vacía desde la Paleta de Comandos ("Python: Crear ventana interactiva"). Esta ventana utilizará el intérprete de Python configurado para tu workspace (es decir, el de tu entorno virtual).
En resumen:

Crea y activa tu entorno virtual (.venv).
Selecciona el intérprete de Python dentro de .venv en VS Code.
Verifica o configura python.pythonPath en la configuración del workspace (settings.json) para que apunte al intérprete de .venv.
Abre la Terminal Integrada (con el entorno activado) y escribe python o usa la Ventana Interactiva de Python de la extensión de Python para ejecutar un REPL dentro de tu entorno virtual.
Siguiendo estos pasos, tu entorno virtual virtualenv (o venv) se convertirá en el entorno predeterminado para tu workspace en VS Code, y podrás utilizar un REPL que se ejecute dentro de ese entorno aislado.

5. Crear un archivo de requisitos
Puede crear un archivo de requisitos que incluya todas las dependencias de su proyecto utilizando el siguiente comando:
```pip freeze > requirements.txt```

6. Instalar paquetes desde un archivo de requisitos
Puede instalar todas las dependencias de su proyecto desde un archivo de requisitos utilizando el siguiente comando:
`pip install -r requirements.txt`
