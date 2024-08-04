import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    # 
    def post(self, endpoint, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, data=data, json=json)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data=None, json=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, data=data, json=json)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, data=data)
        response.raise_for_status()
        return response.json()
