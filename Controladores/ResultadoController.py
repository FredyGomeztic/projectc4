from Modelos.Resultado import Resultado
from Repositorios.ResultadoRepositorio import ResultadoRepositorio

class ResultadoController():
    def __init__(self):
        print("ResultadoController")
        self.resultadoRepositorio = ResultadoRepositorio()

    # Metodo que lista los resultados
    def index(self):
        print("Listado Resultados")
        return self.resultadoRepositorio.findAll()

    # Metodo que consultar un resultado
    def show(self, id):
        print("Consultando resultado ", id)
        result = Resultado(self.resultadoRepositorio.findById(id))
        return result.__dict__

    # Metodo que crea un resultado
    def create(self, aResult):
        print("Creando un resultado")
        result = Resultado(aResult)
        return self.resultadoRepositorio.save(result)

    # Metodo que actualiza un resultado
    def update(self, id, resultado):
        print("Actualizando resultado ", id)
        result = Resultado(self.resultadoRepositorio.findById(id))
        result.mesa = resultado["mesa"]
        result.candidato = resultado["candidato"]
        result.cantidad_votos = resultado["cantidad_votos"]
        return self.resultadoRepositorio.save(result)

    # Metodo que elimina un resultado
    def delete(self, id):
        print("Resultado ", id, " eliminado")
        return self.resultadoRepositorio.delete(id)