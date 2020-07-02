from flask import Flask, jsonify, request
import json

app = Flask(__name__)


desenvolvedores = [
    {'id': 0, 'nome': 'Rafael', 'habilidades': ['Python', 'Flask']},
    {'id': 1, 'nome': 'Galleani', 'habilidades': ['Python', 'Django']},
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def dev(id):

    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'ERRO', 'mensagem': 'Desenvolvedor de ID {} não existe'.format(id)}
        except Exception:
            response = {'status': 'ERRO DESCONHECIDOS', 'mensagem': 'Procure o administrador da API'}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'SUCESSO', 'mensagem': 'Registro'})


@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():

    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == "__main__":
    app.run(debug=True)