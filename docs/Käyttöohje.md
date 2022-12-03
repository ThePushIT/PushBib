## Ohjelman alustus
1. Kloonaa repositorio.
2. Varmista, että koneellesi on asennettuna PostgreSQL, ja käynnistä tietokanta omassa terminaali-ikkunassa. (Jos olet tehnyt asennuksen Tietokantasovellus-kurssin ohjeilla, käynnistäminen onnistuu komennolla `start-pg.sh`.)
3. Jotta ohjelman voisi käynnistää, sille täytyy antaa osoite Postgres-tietokantaan. Osoite välitetään ohjelmalle ympäristömuuttujana `DATABASE_URL`. Repositoriossa on valmiina .env.template-tiedosto. Nimeä tiedosto uudelleen .env-tiedostoksi ja laita tiedostoon osoite tietokantaan. Esimerkiksi voit laittaa tiedostoon `DATABASE_URL=postgresql://` tai `DATABASE_URL=postgresql+psycopg2:///käyttäjätunnus`.
4. Istuntojen käyttäminen vaatii ympäristömuuttujan `SECRET_KEY` asettamisen. Voit muodostaa salaisen avaimen esimerkiksi Pythonin secrets moduulin funktiolla token_hex `secrets.token_hex(16)`. Lisää luotu arvo projektin .env-tiedostoon: `SECRET_KEY=salainenavain`.
5. Asenna projektin riippuvuudet komennolla `poetry install`.
6. Alusta tietokanta komennolla `poetry run python3 src/init_db.py`.

## Ohjelman käynnistys
Siirry poetryn virtuaaliympäristöön suorittamalla komento `poetry shell` ja käynnistä ohjelma komennolla `python3 src/index.py`.

## Testin alustus
1. Avaa psql komentorivi komennolla `psql`
2. Luo uusi testitietokanta kommennolla `create database referencetest`
3. Varmista, että juuresta löytyy tiedosto .env.test, jonka sisältö on 

DATABASE_URL=postgresql+psycopg2:///referencetest

FLASK_ENV = development

4. Alusta testitetokanta ajamalla `poetry run dotenv -f .env.test run -- python3 src/init_db.py`
5. Käynnistä testitietokanta (ajamalla `start-pg.sh`jos asensit tietokannan tällä skriptillä https://github.com/hy-tsoha/local-pg)
6. Käynnistä sovellus ajamalla `poetry run dotenv -f .env.test run -- python3 src/index.py`. Tällöin ympäristömuuttujat haetaan .env.test -tiedostosta eikä .env -tiedostosta.
