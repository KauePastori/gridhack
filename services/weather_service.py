# services/weather_service.py

from external.weather_api_client import WeatherApiClient

class WeatherService:
    def __init__(self):
        self.weather_api_client = WeatherApiClient()

    async def get_current_weather(self):
        return await self.weather_api_client.get_current_weather()
