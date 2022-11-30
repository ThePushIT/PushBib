# Tietokanta
Projektissa käytetään Postgres-tietokantaa, jonka osoite välitetään ohjelmalle ympäristömuuttujana `DATABASE_URL`. Tämä tietokanta alustetaan komennolla `python src/init_db.py`. Tiedostosta näkee myös suurin piirtein tietokannan rakenteen ja taulut. Ne voisi toki myös lisätä tänne kun uusia tauluja luodaan.

## Tietokanta Fly:ssa
Aina kun Fly:hin pusketaan uusi versio, init_db.py suoritetaan ja se yrittää luoda tiedostossa olevat taulut.

## Uusi taulu
Kun haluat luoda uuden taulun, lisää taulun skeema init_db.py-tiedostoon ja suorita init_db.py. Tämä taulu lisätään Fly:n tietokantaan seuraavan kerran kun muokattu tiedosto pusketaan GitHub:in main-haaraan.

## Olemassaolevien taulujen muokkaaminen
Jos haluat muokata olemassaolevaa taulua, niin poista kyseinen taulu omasta tietokannasta ja kirjoita taulun uusi skeema init_db.py-tiedostoon ja suorita se.

__HUOM! Tämä muutos ei näy Fly:n tietokannassa, vaan taulu täytyy vielä erikseen poistaa Fly:n tietokannasta. Lue alemmalta miten saat yhteyden Fly:n tietokantaan.__

## Pääsy Fly:n tietokantaan
Saat avattua Fly:n tietokannan komentokehotteen komennolla 

``fly pg connect --app pushbib-db -t API_AVAIN``

missä API_AVAIN korvataan Fly:n API-avaimella.