import requests

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_reference(self, authors, title, year, publisher):
        data = {
            "authors": authors,
            "title": title,
            "year": year,
            "publisher": publisher
        }

        requests.post(f"{self._base_url}/tests/references/add/1", json=data)