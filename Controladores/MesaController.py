from Modelos.Mesa import Mesa
from Repositorios.MesaRepositorio import MesaRepository

class MesaController():
    def __init__(self):
        print("Construyendo Controlador de Mesa")
        self.mesaRepositorio = MesaRepository()

    # Listado
    def getAll(self):
        response = {}
        try:
            print("Listado de todos las Mesas")
            res = self.mesaRepositorio.findAll()
            response = {
                "length": len(res),
                "msg": "Sin resultados" if len(res) == 0 else "1 resultado" if len(res) == 1 else str(
                    len(res)) + " resultados",
                "result": res
            }
        except:
            response = {
                "err": "Error al consultar",
                "result": []
            }
        return response

    # Creacion
    def create(self, unaMesa):
        response = {}
        try:
            print("Creando la Mesa")
            mesa = Mesa(unaMesa)
            res = self.mesaRepositorio.save(mesa)
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

    #Borrado
    def delete(self,id):
        response = {}
        try:
            print("Borrando Mesa: ", id)
            res = self.mesaRepositorio.delete(id)
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

    #Actualizacion
    def update(self, id, mesa):
        response = {}
        try:
            print("Actualizando la Mesa: ", id)
            mesaActual = Mesa(self.mesaRepositorio.findById(id))
            mesaActual.numero_mesa = mesa["numero_mesa"]
            mesaActual.cantidad_inscritos = mesa["cantidad_inscritos"]
            res = self.mesaRepositorio.save(mesaActual)
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

    #Consulta
    def getById(self, id):
        response = {}
        try:
            print("Consultando Mesa: ", id)
            res = Mesa(self.mesaRepositorio.findById(id))
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