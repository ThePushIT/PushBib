import requests

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def reset_application(self):
        print('reset application funktiota kutsuttu')
        requests.post(f"{self._base_url}/tests/reset/")

    def create_reference(self, authors, title, year, publisher):
        user = 1

        data = {
            "authors": authors,
            "title": title,
            "year": year,
            "publisher": publisher
        }

        requests.post(f"{self._base_url}/tests/references/add/{user}", json=data)