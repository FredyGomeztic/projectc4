from Modelos.Partido import Partido
from Repositorios.PartidoRepositorio import PartidoRepositorio


class PartidoController():
    def __init__(self):
        print("Construyendo controlador de partidos")
        self.partidoRepositorio = PartidoRepositorio()

    # consultar todos los partidos
    def index(self):
        response = {}
        try:
            print("listado de todos los partidos")
            res = self.partidoRepositorio.findAll()
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

    # creacion partido
    def create(self, unPartido):
        response = {}
        try:
            print("creando partido")
            partido = Partido(unPartido)
            res = self.partidoRepositorio.save(partido)
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

    # actualizacion de partido
    def update(self, id, partido):
        response = {}
        try:
            print("actualizando partido", id)
            resultado = Partido(self.partidoRepositorio.findById(id))
            resultado.nombre = partido["nombre"]
            resultado.lema = partido["lema"]
            res = self.partidoRepositorio.save(resultado)
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

    # eliminar un partido
    def delete(self, id):

        response = {}
        try:
            print("eliminando partido", id)
            res = self.partidoRepositorio.delete(id)
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

    # consultar un partido

    def show(self, id):
        response = {}
        try:
            print("consultar un partido")
            res = Partido(self.partidoRepositorio.findById(id))
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
