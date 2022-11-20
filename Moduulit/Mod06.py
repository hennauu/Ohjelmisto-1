#Funktio

#tehtävä 1
import random


def noppa():
    return random.randint(1, 6)


while True:
    x = noppa()
    print(x)
    if x == 6:
        break

#tehtävä 2
import random

tahkot = int(input("Syötä nopan tahkojen määrä: "))


def noppa():
    return random.randint(1, tahkot)


while True:
    x = noppa()
    print(x)
    if x == tahkot:
        break

#tehtävä3
def gallonat_litroina(gallonat):
    litrat = gallonat * 0.2641722
    return litrat


while True:
    gallonat = float(input("Syötä bensiinin määrä gallonina: "))
    if gallonat < 0:
        break
    tulos = gallonat_litroina(gallonat)
    print("Bensiinin määrä litroina: ", tulos)

#tehtävä4
lista = [1, 2, 3, 4, 5]

def luvut(lista):
    summa = sum(lista)
    return summa


print(luvut(lista))

#tehtävä5
lista = [1, 2, 3, 4, 5]

def parittomat(lista):
    for n in lista:
        if n % 2 == 0:
            lista.remove(n)
    return lista


print(lista)
print(parittomat(lista))

#tehtävä6
import math


def pizza(halkaisija, hinta):
    pinta_ala = math.pi * (halkaisija / 2) ** 2
    value = hinta / pinta_ala
    return value


hinta1 = float(input("Syötä 1. pizzan hinta: "))
halkaisija1 = float(input("Syötä 1. pizzan halkaisija metreinä: "))
hinta2 = float(input("Syötä 2. pizzan hinta: "))
halkaisija2 = float(input("Syötä 2. pizzan halkaisija metreinä: "))
value1 = pizza(halkaisija1, hinta1)
value2 = pizza(halkaisija2, hinta2)
print("Ensimmäisen pizzan hinta per neliö: ", value1)
print("Toisen pizzan hinta per neliö: ", value2)
if value1 > value2:
    print("2. pizza on parempi vaihtoehto.")
else:
    print("1. pizza on parempi vaihtoehto.")

