from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir la ruta raíz
@app.route('/')
def hello_world():
    return 'Hola, Mundo!'

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
