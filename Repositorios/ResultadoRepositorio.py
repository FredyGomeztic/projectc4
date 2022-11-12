from Repositorios.RepositorioInterface import RepositorioInterface
from Modelos.Resultado import Resultado
from bson import ObjectId

class ResultadoRepositorio(RepositorioInterface[Resultado]):
    def getTotalVotosPorMesa(self, id_mesa):
        consulta = {}
        if id_mesa != 0:
            consulta = {
                "$match": {"mesa.$id": ObjectId(id_mesa)}
            }
        consulta1 = {
            "$group":{
                "_id": "$mesa",
                "total":{
                    "$sum": "$cantidad_votos"
                },
                "doc": {"$first": "$$ROOT"}
            }
        }
        consulta3 = {
            "$sort": {"total": -1}
        }
        pipeline = [consulta1, consulta3] if id_mesa == 0 else [consulta, consulta1, consulta3]
        result = self.queryAggregation(pipeline)
        response = []
        for n in result:
            total = n.get("total")
            resultado = n.get("doc")
            mesa = resultado.get("mesa")
            id = mesa.get("_id")
            numero_mesa = mesa.get("numero_mesa")
            response.append({
                "id": id,
                "numero_mesa": numero_mesa,
                "total": total
            })
        return response
#https://hispabigdata.blogspot.com/2013/12/como-ordenar-documentos-por-la-suma-de.html