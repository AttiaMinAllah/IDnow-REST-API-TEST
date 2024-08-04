import requests

class APIClient:
    def __init__(self, base_url):
        """
        Initialize the API client with the base URL.
        :param base_url: The base URL for the API.
        """
        self.base_url = base_url

    def get(self, endpoint, params=None):
        """
        Send a GET request to the specified endpoint.

        :param endpoint: The API endpoint.
        :param params: The query parameters for the request.
        :return: The JSON response.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors.
        return response.json()

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
