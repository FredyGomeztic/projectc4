from Repositorios.RepositorioInterface import RepositorioInterface
from Modelos.Partido import Partido


class PartidoRepositorio(RepositorioInterface[Partido]):
    def cantidad_votos_sufragados_por_mesa(self, id_mesa):
        consulta = {
            "$group": {
                "mesa": "$partido",
                "total": {
                    "$sum": "$cantidad_votos"
                },
                "doc": {"$first": "$$ROOT"}
            }
        }
        pipeline = [consulta]
        return self.queryAggregation(pipeline)
