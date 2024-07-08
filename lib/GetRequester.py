import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Ensure we handle HTTP errors properly
        return response.content.decode()  # Return response content as string

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)  # Convert string to JSON and return
