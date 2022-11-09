import pymongo
import certifi
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
from waitress import serve

from Controladores.PartidoController import PartidoController
from Controladores.ResultadoController import ResultadoController
from Controladores.CandidatoController import CandidatoController
from Controladores.MesaController import MesaController

controladorPartido = PartidoController()
controladorResultado = ResultadoController()
controladorCandidato = CandidatoController()
controladorMesa = MesaController()

app = Flask(__name__)
CORS(app)
app.config['ENV'] = "development"

# ************** Mesas ************************
@app.route('/mesa', methods=['POST'])
def crearMesa():
    datos = request.get_json()
    json = controladorMesa.create(datos)
    return jsonify(json)

@app.route('/mesa', methods=['GET'])
def getAllMesas():
    json = controladorMesa.getAll()
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['DELETE'])
def deleteMesa(id):
    json = controladorMesa.delete(id)
    return jsonify(json)

@app.route("/mesa/<string:id>", methods=['PUT'])
def updateMesa(id):
    datos = request.get_json()
    json = controladorMesa.update(id, datos)
    return jsonify(json)

@app.route('/mesa/<string:id>', methods=['GET'])
def getByIdMesa(id):
    json = controladorMesa.getById(id)
    return jsonify(json)



# *****************  Partidos ***************************************************************
# MS Partidos Get all
@app.route("/partido", methods=['GET'])
def getPartidos():
    print("listado de todos los partidos")
    json = controladorPartido.index()
    return jsonify(json)


# MS Partidos Get one
@app.route("/partido/<string:id>", methods=['GET'])
def getPartido(id):
    json = controladorPartido.show(id)
    return jsonify(json)


# MS Partidos Create
@app.route("/partido/", methods=['POST'])
def createPartido():
    print("listado de todos los partidos")
    datos = request.get_json()
    json = controladorPartido.create(datos)
    return jsonify(json)


# MS Partidos Update
@app.route("/partido/<string:id>", methods=['PUT'])
def updatePartido(id):
    datos = request.get_json()
    json = controladorPartido.update(id, datos)
    return jsonify(json)


# MS Partidos Delete
@app.route("/partido/<string:id>", methods=['DELETE'])
def deletePartido(id):
    json = controladorPartido.delete(id)
    return jsonify(json)



# ************** Candidatos *************************************************************
# MS Candidatos Get all
@app.route("/candidato", methods=['GET'])
def getCandidatos():
    json = controladorCandidato.index()
    return jsonify(json)


# MS Candidatos Get one
@app.route("/candidato/<string:id>", methods=['GET'])
def getCandidato(id):
    json = controladorCandidato.show(id)
    return jsonify(json)


# MS Candidatos Create
@app.route("/candidato", methods=['POST'])
def postCandidato():
    datos = request.get_json()
    json = controladorCandidato.create(datos)
    return jsonify(json)


# MS Candidato Update
@app.route("/candidato/<string:id>", methods=['PUT'])
def updateCandidato(id):
    datos = request.get_json()
    json = controladorCandidato.update(id, datos)
    return jsonify(json)


# MS Candidato Delete
@app.route("/candidato/<string:id>", methods=['DELETE'])
def deleteCandidato(id):
    json = controladorCandidato.delete(id)
    return jsonify(json)


# *****************  Resultados ************************************************************
# MS Resultados Get all
@app.route("/resultado/", methods=['GET'])
def getResultados():
    json = controladorResultado.index()
    return jsonify(json)


# MS Resultados Get one
@app.route("/resultado/<string:id>", methods=['GET'])
def getResultado(id):
    json = controladorResultado.show(id)
    return jsonify(json)


# MS Resultados Create
@app.route("/resultado/", methods=['POST'])
def postResultado():
    datos = request.get_json()
    json = controladorResultado.create(datos)
    return jsonify(json)


# MS Resultados Update
@app.route("/resultado/<string:id>", methods=['PUT'])
def updateResultado(id):
    datos = request.get_json()
    json = controladorResultado.update(id, datos)
    return jsonify(json)


# MS Resultados Delete
@app.route("/resultado/<string:id>", methods=['DELETE'])
def deleteResultado(id):
    json = controladorResultado.delete(id)
    return jsonify(json)


#************** Asigna Candidato a Partido ***************
@app.route("/partido/<string:id_partido>/candidato/<string:id_candidato>",methods=['PUT'])
def asignaCandidatoPartido(id_candidato, id_partido):
    json = controladorCandidato.asignarPartido(id_candidato, id_partido)
    return jsonify(json)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
  #  print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def loadConfig():
    with open('config.json') as f:
        datos = json.load(f)
    return datos


if __name__ == '__main__':
    configData = loadConfig()
    print("Server running : "+"http://"+configData["url-backend"]+":" + str(configData["port"]))
    serve(app,host=configData["url-backend"],port=configData["port"])
  #  print('' + configData["url-backend"] + ':' + str(configData["port"]) + "")
 #   serve(app, host=configData["url-backend"], port=configData["port"])
