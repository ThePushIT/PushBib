## Ohjelman alustus
1. Kloonaa repositorio.
2. Varmista, että koneellesi on asennettuna PostgreSQL, ja käynnistä tietokanta omassa terminaali-ikkunassa. (Jos olet tehnyt asennuksen Tietokantasovellus-kurssin ohjeilla, käynnistäminen onnistuu komennolla `start-pg.sh` tai invokella poetry run invoke startdatabase.)
3. Jotta ohjelman voisi käynnistää, sille täytyy antaa osoite Postgres-tietokantaan. Osoite välitetään ohjelmalle ympäristömuuttujana `DATABASE_URL`. Repositoriossa on valmiina .env.template-tiedosto. Nimeä tiedosto uudelleen .env-tiedostoksi ja laita tiedostoon osoite tietokantaan. Esimerkiksi voit laittaa tiedostoon `DATABASE_URL=postgresql://` tai `DATABASE_URL=postgresql+psycopg2:///käyttäjätunnus`.
4. Istuntojen käyttäminen vaatii ympäristömuuttujan `SECRET_KEY` asettamisen. Voit muodostaa salaisen avaimen esimerkiksi Pythonin secrets moduulin funktiolla token_hex `secrets.token_hex(16)`. Lisää luotu arvo projektin .env-tiedostoon: `SECRET_KEY=salainenavain`.
5. Asenna projektin riippuvuudet komennolla `poetry install`.
6. Alusta tietokanta komennolla `poetry run invoke initdb`.

## Ohjelman käynnistys
Käynnistä ohjelma komennolla `poetry run invoke start`.

## Testitietokannan alustus
1. Avaa psql komentorivi komennolla `psql`
2. Luo uusi testitietokanta kommennolla `create database referencetest`
3. Varmista, että juuresta löytyy tiedosto .env.test, jonka sisältö on 

DATABASE_URL=postgresql+psycopg2:///referencetest

FLASK_ENV = development

4. Käynnistä testitietokanta ajamalla `poetry run invoke startdatabase`
5. Alusta testitetokanta ajamalla `poetry run invoke inittestdb`

## Ohjelman ja tietokannan käynnistäminen testejä ajaessa

1. Käynnistä testitietokanta ajamalla `poetry run invoke startdatabase`
2. Käynnistä sovellus ajamalla `poetry run invoke starttestapp`. Tällöin ympäristömuuttujat haetaan .env.test -tiedostosta eikä .env -tiedostosta.

## Testien ajaminen
Yksikkötestit voit ajaa käskyllä `poetry run invoke unittests`. Yksikkötestien haarautumakattavuuden voit testata ajamalla `poetry run invoke coveragereport`. Robottitestit voit ajaa käskyll' `poetry run invoke robottests`.  
