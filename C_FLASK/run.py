from flask import Flask

app = Flask(__name__)


# @app.route("/", method=['GET', 'POST'])
# @app.route("/", method=['POST'])
@app.route("/")
def ola():
    return 'Olá mundo'


"""
@app.route("/<int:numero>")
def ola(numero):
    return 'Olá mundo. {}'.format(numero)
"""


if __name__ == "__main__":
    app.run(debug=True)     # debug = True restarta o código automaticamente