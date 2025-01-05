import math as math

# torke = []
# n = int(input("Unesi broj torki: "))

# for i in range(n):
#   torka= tuple(map(int, input(f"Unesi element torke (odvojene razmakom): ").split() ))
#   torke.append(torka)

# najvecaTorka = None
# najveciZbir = float('-inf')

# for torka in torke:
#   if sum(torka) > najveciZbir:
#     najveciZbir = sum(torka)
#     najvecaTorka = torka
    
# print(f"Torka s najvecim zbirom elemenata: {najvecaTorka}")

# for torka in torke:
#     if all(el % 2 == 0 for el in torka):
#        print(f"Svi elementi su parni ovoj torki: {torka}")

# sortiraneTorke = sorted(torke, key=lambda x : x[1], reverse=True)
# print(f"Sortirane obrnute torke po 2 elemenetu: {sortiraneTorke}")

#######################################
# def prosek(torka):
#   return sum(torka) / len(torka)


# torke = []
# n = int(input("Unesi broj torki: "))

# for i in range(n):
#   torka = tuple(map(float, input("Unesi elemente torke(odvojene razmakom): ").split() ))
#   while len(torka) != 3:  
#     torka = tuple(map(float, input("Torka mora imati 3 elementa(odvojene razmakom): ").split() ))
#   torke.append(torka)

# print(f"Torke: {torke}")
# torke.sort(key=prosek)

# print(f"Sortirane torke prema proseku {torke}")

#######################################

# torke = []
# n = int(input("Unesi broj torki: "))

# for i in range(n):
#   torka = tuple(map(int, input("Unesi torku(elemente odvojene razmakom): ").split() ))
#   while len(torka) != 3:
#     torka = tuple(map(int, input("Torka mora imati 3 elementa: ").split() ))
#   torke.append(torka)

# minRazlika = float('inf')
# najboljaTorka = None

# for torka in torke:
#   razlika = max(torka) - min(torka)
#   if razlika < minRazlika:
#     minRazlika = razlika
#     najboljaTorka = torka

# print(f"Torka s najmanjom razlikom: {najboljaTorka}, razlika: {razlika}")

#######################################
# def provera(torke):
#   parne = []
#   neparne = []
#   for torka in torke:
#     if sum(torka) % 2 == 0:
#       parne.append(torka)
#     else:
#       neparne.append(torka)
#   return parne, neparne

# torke = []
# n = int(input("Unesi broj torki: "))

# for i in range(n):
#   torka = tuple(map(int, input("Unesi elemente torke(odvojene razmakom): ").split() ))
#   while len(torka) != 3:
#     torka = tuple(map(int, input("Torka mora imati 3 elementa: ").split() ))
#   torke.append(torka)

# parneTorke, neparneTorke = provera(torke)

# print(f"Parne torke: {parneTorke}")
# print(f"Neparne torke: {neparneTorke}")
# print(f"Oba torke zajedno: {torke}")

#######################################

# torke = []
# n = int(input("Unesi broj torki: "))

# zbir = float('-inf')
# najvecaTorka = None

# for i in range(n):
#   torka = tuple(map(int, input("Unesi elemente torke(razdvojene razmakom): ").split() ))
#   torke.append(torka)

# for torka in torke:
#   if sum(torka) > zbir:
#     zbir = sum(torka)
#     najvecaTorka = torka
# print(f"Torka {najvecaTorka} ima najveci zbir elemenata: {zbir}")

# for torka in torke:
#   if all(el % 2 == 0  for el in torka):
#     print(f"Torka {torka} ima sve elemente parne.")

# sortiranaTorka = sorted(torke, key=lambda x: x[1], reverse=True)
# print(f"Sortirane torke po i=1 u opadajucem redu: {sortiranaTorka}")

#######################################

# def prosek(torka):
#   return sum(torka) / len(torka)
# torke = []
# n = int(input("Unesi broj torki: "))

# for i in range(n):
#   torka = tuple(map(float, input("Unesi el torke(odvojene razmkaom): ").split() ))
#   while len(torka) != 3:
#     torka = tuple(map(float, input("Torka mora da ima 3 el: ").split() ))
#   torke.append(torka)
# print(f"Unete torke: {torke}")
# torke.sort(key=prosek)

# print(f"Torke: {torke}")
# print(f"Sortirane torke po proseku: {torke}")

#######################################

# n = int(input("Unesi n: "))
# torke = []

# for i in range(n):
#   torka = tuple(map(int,input("Unesi torku(odvojene razmakom): ").split() ))
#   while len(torka) != 3:
#     torka = tuple(map(int,input("Torka mora imati 3 elementa: ").split() ))
#   torke.append(torka)

# minRazlika = float('inf')
# najboljaTorka = None

# for torka in torke:
#   razlika = max(torka) - min(torka)
#   if razlika < minRazlika:
#     minRazlika = razlika
#     najboljaTorka = torka

# print(f"Torka s najmanjom razlikom {najboljaTorka}, razlika {minRazlika}")

#######################################

# def provera(torke):
#   parne = []
#   neparne = []
#   for torka in torke:
#     if sum(torka) % 2 == 0:
#       parne.append(torka)
#     else:
#       neparne.append(torka)
#   return parne, neparne

# n = int(input("Unesi n: "))
# torke = []

# for i in range(n):
#   torka = tuple(map(int,input("Unesi torku(odvojene razmakom): ").split() ))
#   while len(torka) != 3:
#     torka = tuple(map(int,input("Torka mora imati 3 elementa: ").split() ))
#   torke.append(torka)

# parneTorke, neparneTorke = provera(torke)

# print(f"Parne torke: {parneTorke}")
# print(f"Neparne torke: {neparneTorke}")
# print(f"Torke unete: {torke}")

#######################################

# torka = (1,2,3)
# torka2 = (3,4,5)

# sortiraneZajednicki = tuple(sorted(torka+torka2))

# print(sortiraneZajednicki)

#######################################

# torka = (2,5,8,7,6,2,4,8,9,6,2,4,8,9,5)
# parni = []
# for el in torka:
#   if el % 2 == 0:
#     parni.append(el)

# torkaNova = tuple(parni)
# print(torkaNova)

#######################################
# torka1 = []
# torka2 = []
# n = int(input("Unesi dužinu torki: "))

# print("Unos elemenata za prvu torku:")
# for i in range(n):
#     broj = int(input(f"Unesi element {i + 1} prve torke: "))
#     torka1.append(broj)

# print("Unos elemenata za drugu torku:")
# for i in range(n):
#     broj = int(input(f"Unesi element {i + 1} druge torke: "))
#     torka2.append(broj)

# torka1 = tuple(torka1)
# torka2 = tuple(torka2)

# zbirovi = tuple(torka1[i] + torka2[i] for i in range(n))
# razlike = tuple(torka1[i] - torka2[i] for i in range(n))
# proizvodi = tuple(torka1[i] * torka2[i] for i in range(n))

# print(f"Zbir torki: {zbirovi}")
# print(f"Razlika torki: {razlike}")
# print(f"Proizvod torki: {proizvodi}")

#######################################
def suma(torke):
  najvecaSuma = float('-inf')
  najvecaTorka = None
  for torka in torke:
    if sum(torka) > najvecaSuma:
      najvecaSuma = sum(torka)
      najvecaTorka = torka
  return najvecaTorka, najvecaSuma

def sviParni(torke):
  rezultat = []
  for torka in torke:
    parni = True
    for el in torka:
      if el % 2 != 0:
        parni = False
        break
    if parni:
      rezultat.append(torka)
  return tuple(rezultat)


n = int(input("Unesi broj torki: "))
torke = []

for i in range(n):
  torka = tuple(map(int, input("Unesi elemente torke(odvojene razmakom): ").split()))
  torke.append(torka)

maxTorka, maxSum = suma(torke)
parniElementi = sviParni(torke)

sortirana = sorted(torke, key=lambda x :x[1], reverse=True)
print(f"Sortirana: {sortirana}")
print(f"Najveca torka je {maxTorka} a suma je {maxSum}")
print(f"Torke u kojoj su svi el. parni: {parniElementi}")