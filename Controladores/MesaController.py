from Modelos.Mesa import Mesa
from Repositorios.MesaRepositorio import MesaRepository

class MesaController():
    def __init__(self):
        print("Construyendo Controlador de Mesa")
        self.mesaRepositorio = MesaRepository()

    # Listado
    def getAll(self):
        print("Listado de todos las Mesas")
        return self.mesaRepositorio.findAll()

    # Creacion
    def create(self, unaMesa):
        print("Creando la Mesa")
        mesa = Mesa(unaMesa)
        return self.mesaRepositorio.save(mesa)

    #Borrado
    def delete(self,id):
        print("Borrando Mesa: ",id)
        return self.mesaRepositorio.delete(id)

    #Actualizacion
    def update(self, id, mesa):
        print("Actualizando la Mesa: ", id)
        mesaActual = Mesa(self.mesaRepositorio.findById(id))
        mesaActual.numero_mesa = mesa["numero_mesa"]
        mesaActual.cantidad_inscritos = mesa["cantidad_inscritos"]
        return self.mesaRepositorio.save(mesaActual)

    #Consulta
    def getById(self, id):
        print("Consultando Mesa: ", id)
        mesa = Mesa(self.mesaRepositorio.findById(id))
        return mesa.__dict__