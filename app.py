from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola  eres lo maximo Kendy '

if __name__ == '__main__':
    app.run(debug=True)
    

@app.route('/productos/<int:var>')
def saludo_saludo(var):
    return "Mostrar el artículo con id: "+str(var)

@app.route('/contacto')
def saludo_saludo_saludo():
    return 'este es otro mensaje'