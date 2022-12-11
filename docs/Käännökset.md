# Käännökset

## Käännettävien merkkijonojen ilmaisu

### Python
Kun haluat lisätä Python-koodiin jonkin merkkijonon, jolle halutaan tehdä käännös, niin laita se python_babel kirjaston gettext()-funktion parametrina. Eli esimerkiksi kun meillä on alla oleva ohjelma
``` python
print("Hello World!")
```
niin muunna se muotoon
``` python
from flask_babel import gettext

print(gettext("Hello World!"))
```
Tämä on hyödyllinen esimerkiksi virheviestien kohdalla.

### HTML
Kun haluat lisätä nettisivujen pohjalle jotain, joka täytyy kääntää, niin kirjoita se muodossa `{{_('string')}}`. Eli esimerkiksi jos on HTML-tiedosto, joka on muotoa
``` html
<a>Hello World!</a>
```
niin kirjoita se muotoon 
``` html
<a>{{_('Hello World!')}}</a>
```

## Käännöstiedostojen käsittely

### Käännöksien kirjoittaminen
Käännöstiedostot löytyvät kansiosta `translations`, missä jokaiselle kielelle on oma kansio. Käännöksiä voi muokata avaamalla `messages.po`. Alkuperäinen, eli yleensä englanninkielinen, ilmaisu on parametrina msgid: ja sen käännös on sen alapuolella parametrina msgstr:. Eli esimerkiksi käännöstiedostoon kirjoitetaan
```
msgid: Hello World!
msgstr: Hei Maailma!
```

### Uuden kielen käännöstiedosto
Kun haluat luoda jollekin uudelle kielelle käännöstiedoston, niin suorita komento
``` bash
invoke create-translation-file LANGUAGE
```
missä LANGUAGE on jonkin kielen lyhennetty ilmaisu. Esimerkiksi ruotsin kieltä varten komento olisi
``` bash
invoke create-translation-file se
```

Käännöstiedosto luodaan kansioon translations/_LANGUAGE_/LC_MESSAGES

### Käännöstiedostojen päivitys
Kun koodiin on lisätty joitain käännettäviä ilmaisuja, niin ne saa näkyville käännöstiedostoon komennolla
``` bash
invoke update-translation-files
```

### Käännöstiedostojen kompilointi
Jotta käännökset näkyisivät nettisivuilla, ne täytyy aluksi kompiloida. Tämä onnistuu komennolla
``` bash
invoke compile-translations
```

**HUOM! Jos yksittäinen lause ei jostakin syystä näy käännettynä, niin katso käännöstiedostosta että onko kyseisen käännöksen yläpuolella merkintä `#, fuzzy`. Jos on, niin tarkista että käännös on oikein ja poista merkintä.**