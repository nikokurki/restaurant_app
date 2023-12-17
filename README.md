# restaurant_app


Ravintolasovellus
-----------------
Sovellukseen voi lisätä ja arvioida ravintoloita. Sovellukseen kirjaudutaan tunnuksella ja kirjautumisvaihtoehtoja on kaksi: peruskäyttäjä ja ylläpitäjä.

Ominaisuuksia:
1. Käyttäjä voi kirjautua sisään, ulos ja luoda uuden tunnuksen
2. Sovelluksen ensimmäinen käyttäjä on aina ylläpitäjä. Ylläpitäjä pystyy ylentämään muita käyttäjiä ylläpitäjiksi.
3. Käyttäjä voi arvioida ja lukea arvioita ravintoloista
4. Ylläpitäjä voi lisätä ja poistaa ravintoloja
5. Käyttäjä voi etsiä ravintolat sanan perusteella sekä nähdä näistä listauksen parhaimpien arvioiden mukaan
6. Ylläpitäjä voi poistaa arvioita ja luokitella ravintoloita ryhmiin

-----------------
Käyttöohjeet:
Sovellus tarvitsee schema.sql mukaisen tietokantarakenteen ja .env sisältää DATABASE_URL ja SECRET_KEY.

Kloonaa tämä repositorio omalle koneellesi.

Aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt

Määritä vielä tietokannan skeema komennolla

$ psql < schema.sql

Käynnistä sovellus kommennolla

$ flask run




