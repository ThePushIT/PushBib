## Ohjelman alustus
Jotta ohjelman voisi käynnistää, sille täytyy antaa osoite Postgres-tietokantaan. Osoite välitetään ohjelmalle ympäristömuuttujana `DATABASE_URL`. Repositoriossa on valmiina .env.template-tiedosto. Kopioi se samaan kansioon, uudelleennimeä se .env-tiedostoksi ja laita tiedostoon osoite tietokantaan. Esimerkiksi voit laittaa tiedostoon `DATABASE_URL=postgresql://`. Tämän jälkeen suorita komento `python init_db.py` alustaaksesi tietokanta.

Asenna riippuvuudet komennolla `poetry install`.

## Ohjelman käynnistys

Siirry poetryn virtuaaliympäristön sisällä suorittamalla ensiksi `poetry shell` ja käynnistä ohjelma komennolla `python src/index.py`.
