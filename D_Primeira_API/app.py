from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/<int:id>/")
def pessoa(id):
    return jsonify({'id': id, 'nome': 'Leonardo', 'profissao': 'Desenvolvedor'})


"""
@app.route('/soma/<int:valor1>/<int:valor2>/')
def soma(valor1, valor2):
    return jsonify({ 'Soma': valor1 + valor2 })
"""


@app.route('/soma/', method=['POST', 'PUT', 'GET'])
def soma(valor1, valor2):

    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])

    elif request.method == 'GET':
        total = 10 + 10

    return jsonify({'soma': total})


if __name__ == "__main__":
    app.run(debug=True)
