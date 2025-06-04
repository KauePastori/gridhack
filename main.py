from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import network_controller, weather_controller

app = FastAPI(
    title="GridHack API - Simulador de Falhas em Redes Elétricas",
    description="API exemplo para disciplina de Arquitetura Orientada a Serviço (SOA)",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(network_controller.router, prefix="/api/network", tags=["Rede Elétrica"])
app.include_router(weather_controller.router, prefix="/api/weather", tags=["Clima"])
