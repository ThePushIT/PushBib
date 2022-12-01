## Ohjelman alustus
1. Kloonaa repositorio.
2. Varmista, että koneellesi on asennettuna PostgreSQL, ja käynnistä tietokanta omassa terminaali-ikkunassa. (Jos olet tehnyt asennuksen Tietokantasovellus-kurssin ohjeilla, käynnistäminen onnistuu komennolla `start-pg.sh`.)
3. Jotta ohjelman voisi käynnistää, sille täytyy antaa osoite Postgres-tietokantaan. Osoite välitetään ohjelmalle ympäristömuuttujana `DATABASE_URL`. Repositoriossa on valmiina .env.template-tiedosto. Nimeä tiedosto uudelleen .env-tiedostoksi ja laita tiedostoon osoite tietokantaan. Esimerkiksi voit laittaa tiedostoon `DATABASE_URL=postgresql://` tai `DATABASE_URL=postgresql+psycopg2:///käyttäjätunnus`.
4. Istuntojen käyttäminen vaatii ympäristömuuttujan `SECRET_KEY` asettamisen. Voit muodostaa salaisen avaimen esimerkiksi Pythonin secrets moduulin funktiolla token_hex `secrets.token_hex(16)`. Lisää luotu arvo projektin .env-tiedostoon: `SECRET_KEY=salainenavain`.
5. Asenna projektin riippuvuudet komennolla `poetry install`.
6. Alusta tietokanta komennolla `poetry run python3 src/init_db.py`.

## Ohjelman käynnistys
Siirry poetryn virtuaaliympäristöön suorittamalla komento `poetry shell` ja käynnistä ohjelma komennolla `python3 src/index.py`.
