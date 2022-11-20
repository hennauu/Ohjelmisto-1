#Listarakenne ja läpikäyvä toistorakenne (for)

#tehtävä 1
import random

noppa_maara = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(noppa_maara):
    heitto = random.randint(1, 6)
    print(heitto)
    summa += heitto

print("Noppien summa on", summa)

#tehtävä 2
luvut = []

luku = input("Anna luku, jos haluat lopettaa, syötä tyhjä merkkijono (eli paina Enter):")

while luku != "":
    luvut.append(luku)
    luku = input("Anna luku, jos haluat lopettaa, syötä tyhjä merkkijono (eli paina Enter):")

luvut.sort(reverse=True)
print(luvut[0:5])

#tehtävä 3
luku = int(input("Anna kokonaisluku: "))

if luku > 1:
	for i in range(2, int(luku / 2) + 1):
		if (luku % i) == 0:
			print("Antamasi luku ei ole alkuluku.")
			break

	else:
		print(luku, "on alkuluku")

#tehtävä 4
kaupungit = []


for i in range(5):
    kaupungit.append(input("Anna viisi eri kaupunkia (yksi kerrallaan): "))

for i in kaupungit:
    print(i)


