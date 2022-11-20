#Monikko, joukko ja sanakirja

#tehtävä 1
print("Syötä kuukausi numeroina:")
input = input()
x = int(input)


kuukaudet_tupl = (('tammikuu', 'talvi'),
                ('helmikuu', 'talvi'),
                ('maaliskuu', 'kevät'),
                ('huhtikuu', 'kevät'),
                ('toukokuu', 'kevät'),
                ('kesäkuu', 'kesä'),
                ('heinäkuu', 'kesä'),
                ('elokuu', 'kesä'),
                ('syyskuu', 'syksy'),
                ('lokakuu', 'syksy'),
                ('marraskuu', 'syksy'),
                ('joulukuu', 'talvi'))

print("Kuukausi on "
    + kuukaudet_tupl[x-1][0] +
    ", vuodenaika on " + kuukaudet_tupl[x-1][1])

#testi, tehtävä dictionaryna

kuukaudet_dict = {1: {'nimi': 'tammikuu', 'vuodenaika': 'talvi'},
            2: {'nimi': 'helmikuu', 'vuodenaika': 'talvi'},
            3: {'nimi': 'maaliskuu', 'vuodenaika': 'kevät'},
            4: {'nimi': 'huhtikuu', 'vuodenaika': 'kevät'},
            5: {'nimi': 'toukokuu', 'vuodenaika': 'kevät'},
            6: {'nimi': 'kesäkuu', 'vuodenaika': 'kesä'},
            7: {'nimi': 'heinäkuu', 'vuodenaika': 'kesä'},
            8: {'nimi': 'elokuu', 'vuodenaika': 'kesä'},
            9: {'nimi': 'syyskuu', 'vuodenaika': 'syksy'},
            10: {'nimi': 'lokakuu', 'vuodenaika': 'syksy'},
            11: {'nimi': 'marraskuu', 'vuodenaika': 'syksy'},
            12: {'nimi': 'joulukuu', 'vuodenaika': 'talvi'}}


print('Kuukausi on '
+ kuukaudet_dict[x].get('nimi') +
', vuodenaika on ' + kuukaudet_dict[x].get('vuodenaika'))

#tehtävä 2
nimet = set()

while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty.")
    else:
        print("Uusi nimi.")
        nimet.add(nimi)
for nimi in nimet:
    print(nimi)

#tehtävä 3
lentokentat = {}


def lisaa_kentta():
    icao = input("Syötä lentoaseman ICAO-koodi: ")
    nimi = input("Syötä lentoaseman nimi : ")
    lentokentat[icao] = nimi


def etsi_kentta():
    icao_input = input("Syötä kentän ICAO-koodi: ")
    if icao_input in lentokentat:
        nimi = lentokentat[icao_input]
        print(nimi)
    else:
        print("Lentokenttää ei löytynyt.")


while True:
    user_input = input("Kirjoita 'uusi' jos haluat syöttää uuden lentoaseman, 'hae' jos haluat hakea jo syötetyn "
                       "lentoaseman, tai 'lopeta', jos haluat lopettaa. ")
    if user_input.lower() == "uusi":
        lisaa_kentta()
    elif user_input.lower() == "hae":
        etsi_kentta()
    elif user_input.lower() == "lopeta":
        break



