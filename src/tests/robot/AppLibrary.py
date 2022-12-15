import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def reset_application(self):
        print("reset application funktiota kutsuttu")
        requests.post(f"{self._base_url}/tests/reset/")

    def create_reference(self, authors, title, year, publisher):
        user = 1

        data = {
            "authors": authors,
            "title": title,
            "year": year,
            "publisher": publisher
        }

        requests.post(
            f"{self._base_url}/tests/references/book/{user}", json=data)

    def reference_order_should_be(self, page_content, author1, author2, author3):
        position1 = page_content.find(author1)
        position2 = page_content.find(author2)
        position3 = page_content.find(author3)

        return position1 < position2 < position3
