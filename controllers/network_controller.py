from fastapi import APIRouter, HTTPException
from services.network_service import NetworkService

router = APIRouter()
network_service = NetworkService()  # Instância ÚNICA

@router.get("/nodes")
def list_nodes():
    return network_service.get_all_nodes()

@router.post("/nodes/{node_id}/isolate")
def isolate_node(node_id: int):
    success = network_service.isolate_node(node_id)
    if not success:
        raise HTTPException(status_code=404, detail="Só é possível isolar nós em falha.")
    return {"message": f"Nó {node_id} isolado com sucesso. Pronto para ser restaurado."}

@router.post("/nodes/{node_id}/restore")
def restore_node(node_id: int):
    success = network_service.restore_node(node_id)
    if not success:
        raise HTTPException(status_code=404, detail="Só é possível restaurar nós isolados.")
    return {"message": f"Nó {node_id} restaurado com sucesso."}

@router.get("/check-weather-impact")
async def check_weather_impact():
    result = await network_service.check_weather_and_isolate()
    if result["chuva_forte"]:
        return {
            "mensagem": "Chuva forte detectada! Todos os nós foram isolados automaticamente.",
            "weathercode": result["weathercode"],
            "nodes": result["nodes"]
        }
    else:
        return {
            "mensagem": "Sem chuva forte, rede permanece normal.",
            "weathercode": result["weathercode"],
            "nodes": result["nodes"]
        }

@router.post("/disaster")
def trigger_disaster():
    result = network_service.simulate_disaster()
    return result
