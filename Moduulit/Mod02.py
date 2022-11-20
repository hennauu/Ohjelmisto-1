#Muuttujat ja vuorovaikutteiset ohjelmat

#tehtävä 1
kayttaja = input('Mikä sinun nimesi on?: ')
print("Terve, " + kayttaja + "!")

#tehtävä 2
import math
r_str = input("Mikä on ympyrän säde? (m): ")
r = float(r_str)
area = math.pi * r * r
print(f"{r} (m) säteisen ympyrän pinta-ala on n. {area:.3f} neliömetriä.")

#tehtävä 3
kanta = float(input("Mikä on suorakulmion kanta? (m): "))
korkeus = float(input("Mikä on suorakulmion korkeus? (m): "))
area = kanta * korkeus
piiri = 2 * (kanta + korkeus)
print(f"Suorakulmion pinta-ala on {area:.2f} neliömetriä.")
print(f"Suorakulmion piiri on {piiri:.2f} (m).")

#tehtävä 4
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa/3

print(f"Lukujen summa on {summa}, tulo on {tulo} ja keskiarvo on {keskiarvo}.")

#tehtävä 5
leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

mass_g = 13.3 * (luoti + (32 * (naula + (20 * leiviska))))
mass_kg = mass_g/1000
mass_kg_int = int(mass_kg)
grams = ((mass_kg - int(mass_kg)) * 1000)

print(f"Massa nykymittojen mukaan: " + str(mass_kg_int) + " kilogrammaa ja " + str(round(grams, 3)) + " grammaa.")


