import random
from models.node import Node
from services.weather_service import WeatherService

class NetworkService:
    def __init__(self):
        # Dois nós já começam em "Falha"
        self.nodes = [
            Node(id=1, name="Nó 1", status="Falha"),
            Node(id=2, name="Nó 2", status="Falha"),
            Node(id=3, name="Nó 3", status="OK"),
            Node(id=4, name="Nó 4", status="OK"),
            Node(id=5, name="Nó 5", status="OK"),
        ]
        self.weather_service = WeatherService()

    def get_all_nodes(self):
        return self.nodes

    def get_node(self, node_id: int):
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None

    def isolate_node(self, node_id: int):
        node = self.get_node(node_id)
        # Só permite isolar se o nó estiver em Falha
        if node and node.status == "Falha":
            node.status = "Isolado"
            return True
        return False

    def restore_node(self, node_id: int):
        node = self.get_node(node_id)
        # Só permite restaurar se o nó estiver Isolado
        if node and node.status == "Isolado":
            node.status = "OK"
            return True
        return False

    async def check_weather_and_isolate(self):
        weather = await self.weather_service.get_current_weather()
        code = weather["current_weather"]["weathercode"]
        impact = False
        if 80 <= code <= 99:
            for node in self.nodes:
                node.status = "Falha"
            impact = True
        return {
            "chuva_forte": impact,
            "weathercode": code,
            "nodes": [n.dict() for n in self.nodes]
        }

    def simulate_disaster(self):
        num_fail = random.randint(1, 3)
        ok_nodes = [n for n in self.nodes if n.status == "OK"]
        if not ok_nodes:
            return {
                "mensagem": "Todos os nós já estão em falha ou isolados!",
                "nodes": [n.dict() for n in self.nodes]
            }
        nodes_to_fail = random.sample(ok_nodes, min(num_fail, len(ok_nodes)))
        for node in nodes_to_fail:
            node.status = "Falha"
        return {
            "mensagem": f"Desastre natural! {len(nodes_to_fail)} nó(s) falharam!",
            "nodes": [n.dict() for n in self.nodes]
        }
