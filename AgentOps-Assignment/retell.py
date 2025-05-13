import requests


BASE_URL = "http://localhost:8000"  

def get_knowledge(location=None, query_type=None):
    if location:
        response = requests.get(f"{BASE_URL}/api/location?city={location}")
        return response.json()
    elif query_type:
        response = requests.get(f"{BASE_URL}/api/menu?type={query_type}")
        return response.json()
    else:
        return {"error": "Specify location or query_type"}