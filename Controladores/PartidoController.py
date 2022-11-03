from Modelos.Partido import Partido
from Repositorios.PartidoRepositorio import PartidoRepositorio


class PartidoController():
    def __init__(self):
        print("Construyendo controlador de partidos")
        self.partidoRepositorio = PartidoRepositorio()

    # consultar todos los partidos
    def index(self):
        print("listado de todos los partidos")
        return self.partidoRepositorio.findAll()

    # creacion partido
    def create(self, unPartido):
        print("creando partido")
        partido = Partido(unPartido)
        return self.partidoRepositorio.save(partido)

    # actualizacion de partido
    def update(self, id, partido):
        print("actualizando partido", id)
        resultado = Partido(self.partidoRepositorio.findById(id))
        resultado.nombre = partido["nombre"]
        resultado.lema = partido["lema"]
        return self.partidoRepositorio.save(resultado)

    # eliminar un partido
    def delete(self, id):
        print("eliminando partido", id)
        return self.partidoRepositorio.delete(id)

    # consultar un partido

    def show(self, id):
        print("consultar un partido")
        partido = Partido(self.partidoRepositorio.findById(id))
        return partido.__dict__
