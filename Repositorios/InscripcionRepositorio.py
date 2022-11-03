from bson import ObjectId
from Repositorios.RepositorioInterface import RepositorioInterface
from Modelos.Inscripcion import Inscripcion

class InscripcionRepositorio (RepositorioInterface[Inscripcion]):

    def getInscripcionAPartido(self, id_partido):
        consulta = {"partido.$id":ObjectId(id_partido)}
        return self.query(consulta)