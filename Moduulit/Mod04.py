#Alkuehdollinen toistorakenne (while)

#tehtävä 1
alku = 1
loppu = 1000

while alku < loppu and alku % 3 != 0:
    alku = alku + 1
    if alku % 3 == 0:
        print(alku)
        alku = alku + 1

#tehtävä 2
tuuma = int(input("Anna tuumat: "))

cm = 2.51

while tuuma > 0:
    print(tuuma * cm)
    tuuma = int(input("Anna tuumat: "))

    if tuuma < 0:
        print("Ohjelma lopetettu.")

#tehtävä 3
luvut = []


while True:
    luku = input("Anna luku, jos haluat lopettaa ohjelman, paina Enter: ")
    if luku == "":
        break
    luvut.append(float(luku))
    print(luku)
print("Pienin luku: " + str(min(luvut)))
print("Suurin luku: " + str(max(luvut)))

#tehtävä 4
import random
luku = random.randint(1, 10)
arvaus = 0


while arvaus != luku:
    try:
        arvaus = float(input("Arvaa numero: "))
        if luku > arvaus:
            print("Liian pieni arvaus.")
        elif arvaus > luku:
            print("Liian suuri arvaus.")
    except ValueError:
        print("Virheellinen syöte.")
print("Oikein.")

#tehtävä 5
valid_username = "python"
valid_password = "rules"
tryCount = 0
while tryCount < 5:
    tryCount += 1
    input_username = input("Anna käyttäjätunnus: ")
    input_password = input("Anna salasana: ")
    if valid_username == input_username and input_password == valid_password:
        print("Tervetuloa!")
else:
    print("Pääsy evätty.")

#tehtävä 6
import random

pisteiden_maara = int(input("Anna pisteiden määrä: "))
N = 0
n = 0
while N != pisteiden_maara:
    N += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        n += 1
if N == pisteiden_maara:
    pi = 4 * n / N
    print("Piin likiarvo annetuilla pisteillä: " + str(pi))


