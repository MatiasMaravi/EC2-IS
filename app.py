from flask import Flask, request, jsonify,render_template
from utils.calcular import calcular_distancia

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular_distancia', methods=['POST'])
def calcular_distancia_route():
    city1 = request.form.get('city1')
    country1 = request.form.get('country1')
    city2 = request.form.get('city2')
    country2 = request.form.get('country2')
    metodo = request.form.get('metodo')

    distancia = calcular_distancia(city1, country1, city2, country2,metodo)

    return jsonify({'distancia': distancia})

if __name__ == '__main__':
    app.run()