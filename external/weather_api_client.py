# external/weather_api_client.py

import httpx

class WeatherApiClient:
    BASE_URL = "https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current_weather=true"

    async def get_current_weather(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL)
            response.raise_for_status()
            return response.json()
