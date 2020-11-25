from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.Aplicaciones import Aplicacion
import os

app = Flask(__name__)
CORS(app)


@app.route('/aplicaciones', methods=['GET'])
def get():
    return Aplicacion.getAll()


@app.route('/aplicaciones', methods=['POST'])
def post():
    body = request.json
    return Aplicacion.post(body)


@app.route('/aplicaciones/<idApp>/', methods=['PUT'])
def put(idApp):
    body = request.json
    return Aplicacion.put(idApp, body)


@app.route('/aplicaciones/<idApp>/', methods=['DELETE'])
def delete(idApp):
    return Aplicacion.delete(idApp)


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)
