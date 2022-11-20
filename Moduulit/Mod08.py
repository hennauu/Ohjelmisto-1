#Relaatiotietokannan käyttö

#tehtävä 1
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='henna',
         autocommit=True
         )

icao = input("Anna lentoaseman ICAO-koodi: ")
sql = "SELECT name, municipality FROM airport WHERE ident = '" + icao + "'"
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")



#tehtävä 2
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='henna',
         autocommit=True
         )

aa = input("Maakoodi : ")
sql = "SELECT type, count(*) FROM airport WHERE iso_country = '" + maa + "' GROUP BY type"
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")

#tehtävä 3
import mysql.connector
import geopy.distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='henna',
         autocommit=True
         )

icao_1 = input("Anna lentokentän 1 ICAO-koodi : ")
sql_1 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + icao_1 + "'"
kursori = yhteys.cursor()
kursori.execute(sql_1)
tulos = kursori.fetchall()
for rivi in tulos:
    lat_1 = rivi[0]
    lon_1 = rivi[1]
airport_1 = (lat_1, lon_1)

icao_2 = input("Anna lentokentän 2 ICAO-koodi : ")
sql_2 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + icao_2 + "'"
kursori = yhteys.cursor()
kursori.execute(sql_2)
tulos = kursori.fetchall()
for rivi in tulos:
    lat_2 = rivi[0]
    lon_2 = rivi[1]
airport_2 = (lat_2, lon_2)

print(geopy.distance.distance(airport_1, airport_2).km)

