import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "c1adaf3e7d3ee032b8f8e2d56be5d0fa"   # Replace with your own

def test_valid_city():
    params = {"q": "London", "appid": API_KEY}
    response = requests.get(BASE_URL, params=params)
    print(response.status_code, response.text)
    assert response.status_code == 200
    data = response.json()
    assert "weather" in data
    assert "main" in data

def test_invalid_city():
    params = {"q": "NoSuchCity", "appid": API_KEY}
    response = requests.get(BASE_URL, params=params)
    print(response.status_code, response.text)
    data = response.json()
    assert str(data.get("cod")) == "404"
    assert "city not found" in data.get("message", "").lower()

def test_missing_api_key():
    params = {"q": "London"}
    response = requests.get(BASE_URL, params=params)
    print(response.status_code, response.text)
    data = response.json()
    assert str(data.get("cod")) == "401"
    assert "invalid api key" in data.get("message", "").lower()
