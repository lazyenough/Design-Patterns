from abc import ABC, abstractmethod


class WeatherProvider(ABC):
    @abstractmethod
    def get_weather(self, location: str):
        pass
    

class APIWeatherProvider(WeatherProvider):
    def get_weather(self, location):
        return f"Weather detais from API for {location}."
    
class FileWeatherProvider(WeatherProvider):
    def get_weather(self, location):
        return f"Weather detais from File for {location}."
    
class MockWeatherProvider(WeatherProvider):
    def get_weather(self, location):
        return f"Weather detais from Mock system for {location}."


class WeatherService:
    def __init__(self, provider: WeatherProvider):
        self.provider = provider
    
    def fetch_weather(self, location):
        return self.provider.get_weather(location)
    

if __name__ == "__main__":
    api_provider = WeatherService(APIWeatherProvider())
    print(api_provider.fetch_weather("Delhi"))
    
    file_provider = WeatherService(FileWeatherProvider())
    print(file_provider.fetch_weather("Pune"))
    
    mock_provider = WeatherService(MockWeatherProvider())
    print(mock_provider.fetch_weather("Kochi"))
        