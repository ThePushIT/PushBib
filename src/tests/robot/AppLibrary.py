import requests

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_reference(self, name, authors, year):
        user = 1

        data = {
            "name": name,
            "authors": authors,
            "year": year
        }

        requests.post(f"{self._base_url}/tests/references/add/{user}", json=data)