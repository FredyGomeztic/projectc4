from Modelos.Candidato import Candidato
from Repositorios.CandidatoRepositorio import CandidatoRepositorio

class CandidatoController():
    def __init__(self):
        print("Candidato Controller")
        self.CandidatoRepositorio = CandidatoRepositorio()

    # Metodo que lista los Candidatos
    def index(self):
        print("Listado Candidatos")
        return self.CandidatoRepositorio.findAll()

    # Metodo que consultar un Candidato
    def show(self, id):
        print("Consultando Candidatos ", id)
        result = Candidato(self.CandidatoRepositorio.findById(id))
        return result.__dict__

    # Metodo que crea un Candidato
    def create(self, candidato):
        print("Creando un Candidato")
        result = Candidato(candidato)
        return self.CandidatoRepositorio.save(result)

    # Metodo que actualiza un Candidato
    def update(self, id, candidato):
        print("Actualizando resultado ", id)
        result = Candidato(self.CandidatoRepositorio.findById(id))
        result.cedula= candidato["cedula"]
        result.nombre = candidato["nombre"]
        result.apellido = candidato["apellido"]
        result.partido = candidato["partido"]
        result.numeresolucion = candidato["numeresolucion"]
        return self.CandidatoRepositorio.save(result)

    # Metodo que elimina un Candidato
    def delete(self, id):
        print("Candidato ", id, " eliminado")
        return self.CandidatoRepositorio.delete(id)