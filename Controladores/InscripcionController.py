from Modelos.Inscripcion import Inscripcion
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
from Repositorios.InscripcionRepositorio import InscripcionRepositorio
from Repositorios.PartidoRepositorio import PartidoRepositorio
from Repositorios.CandidatoRepositorio import CandidatoRepositorio

class InscripcionController ():

    def __init__(self):
        print("Creando Controlador para asignar partido a Candidato")
        self.repoPartido = PartidoRepositorio()
        self.repoCandidato = CandidatoRepositorio()
        self.repoInscripcion = InscripcionRepositorio()
    
    def index(self):
        print("Listando las inscripciones de candidatos a un Partido")
        return self.repositorio.findAll()

  # **** Asignando Partido a Candidato ****      

    def create(self, dataInscripcion, id_partido, id_candidato):
        inscripcion = Inscripcion(dataInscripcion)
        candidato = Candidato(self.repoCandidato.findById(id_candidato))
        partido = Partido(self.repoPartido.findById(id_partido))
        inscripcion.partido = partido
        inscripcion.candidato = candidato

        return self.repoInscripcion.save(inscripcion)

        