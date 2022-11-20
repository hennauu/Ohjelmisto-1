#Valintarakenne (if)

#1 tehtävä
pituus = float(input("Kuinka pitkä kuha on (cm)?"))
pyyntimitta = 37
if pituus < pyyntimitta:
    print(f"Laske kuha takaisin järveen, sallitusta pyyntimitasta puuttuu {pyyntimitta - pituus} cm")
if pituus >= pyyntimitta:
    print(f"Kalasi on pyyntimittainen, voit pitää sen!")

#2 tehtävä
hyttiluokka = input("Mikä on hyttiluokkasi?").upper()
if hyttiluokka == "LUX":
    print(f"LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print(f"A on ikkunallinen hytti autokannen yläpuolella")
elif hyttiluokka == "B":
    print(f"B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print(f"C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")

#3 tehtävä

sukupuoli = input("Mikä on biologinen sukupuolesi?")
if sukupuoli == "nainen" or sukupuoli == "mies":
    hemoglobiini = int(input("Mikä on hemoglobiiniarvosi?"))
if (hemoglobiini >= 117 and hemoglobiini <= 175 and sukupuoli == "nainen"):
    print(f"Hemoglobiiniarvosi on normaali")
elif (hemoglobiini < 117 and sukupuoli == "nainen"):
    print(f"Hemoglobiiniarvosi on liian alhainen")
elif (hemoglobiini > 175 and sukupuoli == "nainen"):
    print(f"Hemoglobiiniarvosi on liian korkea")
elif (hemoglobiini >= 134 and hemoglobiini <= 195 and sukupuoli == "mies"):
    print(f"Hemoglobiiniarvosi on normaali")
elif (hemoglobiini < 134 and sukupuoli == "mies"):
    print(f"Hemoglobiiniarvosi on liian alhainen")
elif (hemoglobiini > 195 and sukupuoli == "mies"):
    print(f"Hemoglobiiniarvosi on liian korkea")

#4 tehtävä

vuosi = int(input("Syötä vuosiluku: "))
if (vuosi % 400 == 0) and (vuosi % 100 == 0):
    print("{0} on karkausvuosi".format(vuosi))
elif (vuosi % 4 == 0) and (vuosi % 100 != 0):
    print("{0} on karkausvuosi".format(vuosi))



