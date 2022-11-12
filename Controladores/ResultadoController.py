from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Repositorios.ResultadoRepositorio import ResultadoRepositorio
from Repositorios.CandidatoRepositorio import CandidatoRepositorio
from Repositorios.MesaRepositorio import MesaRepository

class ResultadoController():
    def __init__(self):
        print("ResultadoController")
        self.resultadoRepositorio = ResultadoRepositorio()
        self.candidatoRepositorio = CandidatoRepositorio()
        self.mesaRepositorio = MesaRepository()

    # Metodo que lista los resultados
    def index(self):
        response = {}
        try:
            print("Listado Resultados")
            res = self.resultadoRepositorio.findAll()
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

    # Metodo que consultar un resultado
    def show(self, id):
        response = {}
        try:
            print("Consultando resultado ", id)
            res = Resultado(self.resultadoRepositorio.findById(id))
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

    # Metodo que crea un resultado
    def create(self, resultado):
        response = {}
        try:
            print("Creando un resultado")
            result = Resultado(resultado)
            if "candidato" in resultado:
                result.candidato = Candidato(self.candidatoRepositorio.findById(resultado["candidato"]))
            if "mesa" in resultado:
                result.mesa = Mesa(self.mesaRepositorio.findById(resultado["mesa"]))
            res = self.resultadoRepositorio.save(result)
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

    # Metodo que actualiza un resultado
    def update(self, id, resultado):
        response = {}
        try:
            print("Actualizando resultado ", id)
            result = Resultado(self.resultadoRepositorio.findById(id))
            result.cantidad_votos = resultado["cantidad_votos"]
            if "mesa" in resultado:
                result.mesa =Mesa(self.mesaRepositorio.findById(resultado["mesa"]))
            if "candidato" in resultado:
                result.candidato = Candidato(self.candidatoRepositorio.findById(resultado["candidato"]))
            res = self.resultadoRepositorio.save(result)
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

    # Metodo que elimina un resultado
    def delete(self, id):
        response = {}
        try:
            print("Resultado ", id, " eliminado")
            res = self.resultadoRepositorio.delete(id)
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

    def totalVotosPorMesa(self, id_mesa):
        response = {}
        try:
            print("totalVotosPorMesa ", id_mesa, " consultando")
            res = self.resultadoRepositorio.getTotalVotosPorMesa(id_mesa)
            response = {
                "msg": "Sin resultados" if len(res) == 0 else "1 resultado" if len(res) == 1 else str(len(res)) + " resultados",
                "result": res if id_mesa == 0 else res[0]
            }
            if id_mesa == 0:
                response.update({"length": len(res)})
        except:
            response = {
                "err": "Ocurrió un error en la consulta",
                "result": False
            }
        return response