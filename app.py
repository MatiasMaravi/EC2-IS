from flask import Flask, request, jsonify,render_template
from factory import Factory

app = Flask(__name__)
#Registramos todos nuestros builders
factory = Factory()
factory.load()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular_distancia', methods=['POST'])
def calcular_distancia_route():
    response = request.form.to_dict()
    objeto = factory.create(response['metodo'])
    distancia = objeto.calcular_distancia(response['city1'],response['country1'],response['city2'],response['country2'])
    return jsonify({'distancia': distancia})

if __name__ == '__main__':
    app.run()