from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
from Repositorios.CandidatoRepositorio import CandidatoRepositorio
from Repositorios.PartidoRepositorio import PartidoRepositorio

class CandidatoController():
    def __init__(self):
        print("Candidato Controller")
        self.CandidatoRepositorio = CandidatoRepositorio()
        self.PartidoRepositorio = PartidoRepositorio()

    # Metodo que lista los Candidatos
    def index(self):
        response = {}
        try:
            print("Listado Candidatos")
            res = self.CandidatoRepositorio.findAll()
            response = {
                "length": len(res),
                "msg": "Sin resultados" if len(res) == 0 else "1 resultado" if len(res) == 1 else str(len(res)) + " resultados",
                "result": res
            }
        except:
            response = {
                "err": "Error al consultar",
                "result": []
            }
        return response

    # Metodo que consultar un Candidato
    def show(self, id):
        response = {}
        try:
            print("Consultando Candidatos ", id)
            res = Candidato(self.CandidatoRepositorio.findById(id))
            response = {
                "msg": "1 resultado",
                "result": res.__dict__
            }
        except:
            response = {
                "err": "Error al consultar",
                "msg": "Sin resultados",
                "result": {}
            }
        return response

    # Metodo que crea un Candidato
    def create(self, candidato):
        response = {}
        try:
            print("Creando un Candidato")
            result = Candidato(candidato)
            if "partido" in candidato:
                partido = Partido(self.PartidoRepositorio.findById(candidato["partido"]))
                result.partido = partido
            res = self.CandidatoRepositorio.save(result)
            response = {
                "msg": "Registro exitoso",
                "result": True
            }
        except:
            response = {
                "err": "Error al registrar",
                "msg": "Ocurrió un error, verifique los datos",
                "result": False
            }
        return response

    # Metodo que actualiza un Candidato
    def update(self, id, candidato):
        response = {}
        try:
            print("Actualizando resultado ", id)
            result = Candidato(self.CandidatoRepositorio.findById(id))
            result.cedula = candidato["cedula"]
            result.nombre = candidato["nombre"]
            result.apellido = candidato["apellido"]
            result.numero_resolucion = candidato["numero_resolucion"]
            if "partido" in candidato:
                result.partido = Partido(self.PartidoRepositorio.findById(candidato["partido"]))
            res = self.CandidatoRepositorio.save(result)
            response = {
                "msg": "Actualización exitosa",
                "result": True
            }
        except:
            response = {
                "err": "Error al actualizar",
                "msg": "Ocurrió un error, verifique los datos",
                "result": False
            }
        return response

    # Metodo que elimina un Candidato
    def delete(self, id):
        response = {}
        try:
            print("Candidato ", id, " eliminado")
            res = self.CandidatoRepositorio.delete(id)
            response = {
                "msg": "Registro eliminado",
                "result": True
            }
        except:
            response = {
                "err": "Error al eliminar",
                "msg": "Ocurrió un error, verifique los datos",
                "result": False
            }
        return response