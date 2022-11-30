# Arkkitehtuuri
Ohjelmassa käytetään kerrosarkkitehtuuria.

## Käyttöliittymä
Kaikki käyttöliittymään liittyvä koodi on controllers-kansion sisällä. Kyseinen kansio sisältää Flaskin "blueprintejä", jotka sisältävät polut, jotka Flask ymmärtää sekä niihin liittyvä koodi. Tämän voi kuvitella niin, että kun tsoha:ssa tehtiin `routes.py` tiedosto, joka sisälsi kaikki polut, niin tässä kyseinen tiedosto jaetaan useampaan tiedostoon name_controller.py-tiedostoon. Mallin voi katsoa controllers/hello_controller.py tiedostosta. Jos luo uuden controllerin (esimerkiksi new_controller.py), niin se täytyy vielä rekisteröidä itse ohjelmaan lisäämällä app.py-tiedostoon `app.register_blueprint(new_controller.py)`.