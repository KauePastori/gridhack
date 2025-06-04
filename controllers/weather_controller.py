# controllers/weather_controller.py

from fastapi import APIRouter
from services.weather_service import WeatherService

router = APIRouter()
weather_service = WeatherService()

@router.get("/current")
async def get_current_weather():
    return await weather_service.get_current_weather()
