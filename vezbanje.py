import math as math

# nizA = []
# nizB = []
# nizC = []

# n = int(input("Unesi n: "))
# while n >= 200:
#   n = int(input("N mora biti manje od 200: "))

# print("Unesi elemente za niz A")
# for i in range(n):
#   a = int(input("Unesi element nizaA: "))
#   nizA.append(a)

# print("Unesi elemente za niz B")
# for i in range(n):
#   b = int(input("Unesi element nizaB: "))
#   nizB.append(b)

# print("Niz C:")
# for i in range(n):
#   nizC.append(max(nizA[i],nizB[i]))

# print(f"Niz A: {nizA}")
# print(f"Niz B: {nizB}")
# print(f"Niz C: {nizC}")
#######################################
# niz = []
# n = int(input("Unesi n (3-100): "))

# while n < 3 or n > 100:
#   n = int(input("N mora biti pozitivan i veci od 3 a manji od 100: "))

# for i in range(n):
#   el = float(input("Unesi element: "))
#   niz.append(el)

# for i in range(1, len(niz)-1):
#   if niz[i] == (niz[i-1] + niz[i+1])/2:
#     print(f"Element {niz[i]} s indeksom {i+1} je aritmeticka sredina")

#######################################
# def obimPoligona(nizA,nizB, n):
#   obim = 0
#   for i in range(n):
#     obim += math.sqrt((nizA[(i+1) % n] - nizA[i])**2 + (nizB[(i+1) % n] - nizB[i])**2)
#   return obim

# nizA = []
# nizB = []
# n = int(input("Unesi n kao broj kordinata temena x i y: "))

# for i in range(n):
#   element = float(input("Unesi element nizaA: "))
#   nizA.append(element)
  
# for i in range(n):
#   element = float(input("Unesi element nizaB: "))
#   nizB.append(element) 

# Obim = obimPoligona(nizA, nizB, n)

# print(f"Obim: {Obim}")
#######################################

# unos = input("Unesi hex broj: ")

# validniKarakteri = "0123456789ABCDEFabcdef"


# while not all(char in validniKarakteri for char in unos) or len(unos) > 6:
#   unos = input("Unesi hex broj:(1-9,A...F, manje od 6 karaktera) ")

# toDecimal = int(unos, 16)
# print(f"Decimalan broj: {toDecimal}")
#######################################
# def palindrom():
#   while True:
#     unos = input("Unesi neku rec za proveru: ")
#     if unos == "":
#      print("Unos je prazan")
#      break
#     if unos[:] == unos[::-1]:
#       print("PALINDROM")
#     else:
#       print("NIJE PALINDROM")      


# provera = palindrom()
# print(f"Palindrom: {provera}")
#######################################
# def duzinaIzlomljenjeLinije(x,y,n):
#   duzina = 0
#   for i in range(n-1):
#     duzina += math.sqrt((x[i+1] - x[i])**2 +(y[i+1] - y[i])**2)
#   return duzina


# while True:
#   n = int(input("Unesi broj tacaka, najmanje 2: "))
#   if n < 2:
#     print("Prekid, nevalidan unos")
#     break

#   x = []
#   y = []

#   for i in range(n):
#     xElementi = int(input("Unesi elemete x niza: ")) 
#     yElementi = int(input("Unesi elemete y niza: ")) 
#     x.append(xElementi)
#     y.append(yElementi)

#   duzina = duzinaIzlomljenjeLinije(x,y,n)
#   print(f"Duzina izlomljenje linije {duzina}")
#######################################
# redovi = int(input("Unesi redove: "))
# kolone = int(input("Unesi kolone: "))

# zbirGlavne = 0
# minElement = float('inf')
# matrica = []

# print("Unesi matricu: ")
# for i in range(redovi):
#   red = []
#   for j in range(kolone):
#     element = int(input(f"Unesi elemente matrice [{i}][{j}](1,2,5,10,20): "))
#     red.append(element)
#     if i == j:
#       zbirGlavne += element
#     if j > i:
#       if element < minElement:
#         minElement = element

#   matrica.append(red)

# print("Uneta matrica: ")
# for red in matrica:
#   for el in red:
#     print(el, end=" ")
#   print()

# print(f"Zbir el. glavne dijagonale: {zbirGlavne}")
# print(f"Min el. iznad glavne dijagonale: {minElement}")
#######################################
# n = int(input("Unesi n torki: "))

# torke = []

# for i in range(n):
#   torka = tuple(map(int, input(f"Unesi element torke {i+1}: ").split()))
#   torke.append(torka)

# najveciZbir = -float('inf')
# maxTorka = None

# for torka in torke:
#   zbir = sum(torka)
#   if zbir > najveciZbir:
#     najveciZbir = zbir
#     maxTorka = torka

# for torka in torke:
#   sviParni = True
#   for element in torka:
#     if element % 2 != 0:
#       sviParni = False
#       break
#   if sviParni:
#     print(f"Elementi kod ove torke: {torka} su  parni")

# sortiraneTorke = sorted(torke, key=lambda  torka:torka[1], reverse=True )
# print(f"Torka s najvecim zbirom el iznosi: {najveciZbir} a ona je {maxTorka}")
# print(f"Sortirane torke po 2 elementu: {sortiraneTorke}")
#######################################
# n = int(input("Unesi n redove: "))
# m = int(input("Unesi m kolone: "))
# matrica = []

# print("Unesi matricu: ")
# for i in range(n):
#   red = []
#   for j in range(m):
#     element = int(input(f"Unesi elemente matrice [{i}][{j}]: "))
#     red.append(element)
#   matrica.append(red)

# print("Prikaz matrice: ")
# for red in matrica:
#   for el in red:
#     print(el, end = " ")
#   print()

# maxEl = matrica[0][0]
# minEl = matrica[0][0]

# for red in matrica:
#   for el in red:
#     if el > maxEl:
#       maxEl = el
#     if el < minEl:
#       minEl = el

# print(f"Max el. : {maxEl}")
# print(f"Min el. : {minEl}")

# maxRedIndex = -1
# minRedIndex = -1

# for i, red in enumerate(matrica):
#   if maxEl in red:
#     maxRedIndex = i
#   if minEl in red:
#     minRedIndex = i

# print(f"Red s najvecim elmentom: {matrica[maxRedIndex]}")
# print(f"Red s najmanjim elmentom: {matrica[minRedIndex]}")

# matrica[maxRedIndex], matrica[minRedIndex] = matrica[minRedIndex], matrica[maxRedIndex]

# print("Prikaz nove matrice: ")
# for red in matrica:
#   for el in red:
#     print(el, end = " ")
#   print()
#######################################
# n = int(input("Unesi n za kvadratnu jednacinu: "))
# matrica = []
# zbirSporedne = 0
# minEl = float('inf')

# print("Unesi matricu: ")
# for i in range(n):
#   red = []
#   for j in range(n):
#     element = int(input(f"Unesi element [{i}][{j}]: "))
#     red.append(element)
#     if j == n-i-1:
#       zbirSporedne += element
#     if j<n-i-1 and element < minEl:
#         minEl = element
#   matrica.append(red)

# print("Prikaz matrice: ")
# for red in matrica:
#   for el in red:
#     print(el, end = " ")
#   print()

# print(f"Suma el sporedne dijagonale {zbirSporedne}")
# print(f"Min el iznad sporedne dijagonale {minEl}")

#######################################

# n = int(input("Unesi n za kvadratnu jednacinu: "))
# while n <= 1 or n >= 10:
#   n = int(input("Unesi n u opsegu od 1 do 10: "))

# matrica = []

# print("Unesi matricu: ")
# for i in range(n):
#   red = []
#   for j in range(n):
#     element = int(input(f"Unesi element [{i}][{j}]: "))
#     red.append(element)
#   matrica.append(red)

# print("Prikaz matrice: ")
# for red in matrica:
#   for el in red:
#     print(el, end = " ")
#   print()

# print("Nova matrica: ")
# for i in range(n):
#   for j in range(i, n):
#     matrica[i][j], matrica[j][i] = matrica[j][i], matrica[i][j]
  
# for i in range(n):
#   matrica[i].reverse()

# print("Prikaz matrice: ")
# for red in matrica:
#   for el in red:
#     print(el, end = " ")
#   print()

#######################################

# n = int(input("Unesi n za kvadratnu matricu: "))

# matrica = []

# print("Unesi matricu: ")
# for i in range(n):
#   red = []
#   for j in range(n):
#     element = int(input("Unesi el matrice: "))
#     red.append(element)
#   matrica.append(red)

# print("Matrica: ")
# for red in matrica:
#   for el in red:
#     print(el, end= " ")
#   print()

# transponovana = []
# print("Transponovana matrica: ")
# for i in range(n):
#   red = []
#   for j in range(n):
#     red.append(matrica[j][i])
#   transponovana.append(red)

# for red in transponovana:
#   print(red)

#######################################

# n = int(input("Unesi n: (vrsta)"))
# m = int(input("Unesi m: (kolona)"))

# while n <= 1:
#   n = int(input("Ponovo unesi n: (n>1) "))

# while m >= 10:
#   m = int(input("Ponovo unesi m: (m<10) "))

# matrica = []
# print("Unesi matricu: ")
# for i in range(n):
#   red = []
#   for j in range(m):
#     element = int(input("Unesi el matrice: "))
#     red.append(element)
#   matrica.append(red)

# print("Matrica: ")
# for red in matrica:
#   for el in red:
#     print(el, end= " ")
#   print()

# for i in range(n):
#   minEl = matrica[i][0]
#   minKolona = 0
#   for j in range(m):
#     if matrica[i][j] < minEl:
#       minEl = matrica[i][j]
#       minKolona = j
  
#   isBiggest = True

#   for k in range(n):
#     if matrica[k][minKolona] > minEl:
#       isBiggest = False
#       break

#   if isBiggest:
#     print(f"Sedlasta tacka: {minEl} na poziciji {i}, {minKolona}")

#######################################
# def prosekTorke(torke):
#    proseci = []
#    for torka in torke:
#       s = sum(torka)
#       proseci.append(s / 3)
#    return proseci
         
# torke = []
# n = int(input("Unesi broj torki: "))

# for i in range(n):
#     while True:
#       el = input("Unesi element torke, odvojene razmakom: ").split()
#       if len(el) == 3:
#          torka = tuple(map(float, el))
#          torke.append(torka)
#          break
#       else:
#         print("Torka mora imati tacno 3 elementa.")

# prosekTorki = prosekTorke(torke)
# sortiraneTorkePoProseku = sorted(torke, key=lambda t : sum(t) / len(t), )
# print(torke)
# print(f"Prosek svake torke {prosekTorki}")
# print(f"Sortirane torke {sortiraneTorkePoProseku}")

#######################################

# def provera(torke):
#   najmanjaRazlika = float('inf')
#   najboljaTorka = None
#   for torka in torke:
#     minEl = min(torka)
#     maxEl = max(torka)
#     razlika = maxEl - minEl
#     if razlika < najmanjaRazlika:
#       najmanjaRazlika = razlika
#       najboljaTorka = torka
#   return najboljaTorka
  
# torke = []
# n = int(input("Unesi broj torki: "))

# for i in range(n):
#   while True:
#     element = input("Unesi elemente torke, razdovojene razmakom: ").split()
#     if len(element) == 3:
#       torka = tuple(map(int, element))
#       torke.append(torka)
#       break
#     else:
#       print("Torka mora imati 3 elementa!")

# najmanjaTorka = provera(torke)
# print(torke)
# if najmanjaTorka:
#   print(f"Torka sa najmanjom razlikom izmedju najveceg i najmanjeg elementa: {najmanjaTorka}")
# else:
#   print("Greska!")


#######################################

# matrica = []
# n = int(input("Unesi vrstu: "))
# m = int(input("Unesi kolonu: "))

# najveciEl = float('-inf')
# najmanjiEl = float('inf')

# vrstaNajveci = -1
# vrstaNajmanji = -1

# print("Unesi matricu: ")
# for i in range(n):
#   red = []
#   for j in range(m):
#     el = int(input(f"Unesi element[{i}][{j}]: "))
#     red.append(el)
#   matrica.append(red)

# print("Matrica: ")
# for red in matrica:
#   for element in red:
#     print(element, end= " ")
#   print()

# for i, vrsta in enumerate(matrica):
#   maxEl = max(vrsta)  
#   minEl = min(vrsta)

#   if maxEl > najveciEl:
#     najveciEl = maxEl
#     vrstaNajveci = i

#   if minEl < najmanjiEl:
#     najmanjiEl = minEl
#     vrstaNajmanji = i 

# print(f"Najveci el {najveciEl} u vrsti {vrstaNajveci+1}")
# print(f"Najmanji el {najmanjiEl} u vrsti {vrstaNajmanji+1}")
# matrica[vrstaNajmanji], matrica[vrstaNajveci] = matrica[vrstaNajveci], matrica[vrstaNajmanji]

# print("Nova matrica: ")
# for red in matrica:
#   for el in red:
#     print(el, end=" ")
#   print()

#######################################

# n = int(input("Unesi n: "))
# matrica = []
# maxEl = float('-inf')

# for i in range(n):
#   red = []
#   for j in range(n):
#     el = int(input(f"Unesi element[{i}][{j}]: "))
#     red.append(el)
#   matrica.append(red)

# print("Matrica: ")
# for red in matrica:
#   for el in red:
#     print(el, end= " ")
#   print()

# for i in range(n):
#   s = 0
#   for j in range(n):
#     if j == n-1-i:
#       s += matrica[i][j]

# for i in range(n):
#   for j in range(n):
#     if j < n-1-i:
#       if matrica[i][j] > maxEl:
#         maxEl = matrica[i][j]
    
# print(f"Najveci element iznad sporedne dijagonale {maxEl}")

#######################################

# n = int(input("Unesi n: "))
# matrica = []
# while n > 10 or n < 1:
#   n = int(input("N mora biti u opsegu 1<=n<=10: "))

# for i in range(n):
#   red = []
#   for j in range(n):
#     el = int(input(f"Unesi element matrice[{i}][{j}]: "))
#     red.append(el)
#   matrica.append(red)

# print("Matrica: ")
# for red in matrica:
#   for el in red:
#     print(el, end=" ")
#   print()
# for red in matrica:
#   for el in red:
#     print(el, end=" ")
#   print()

# for i in range(n):
#   for j in range(i,n):
#     matrica[i][j],matrica[j][i] = matrica[j][i], matrica[i][j]

# for i in range(n):
#   matrica[i].reverse()

# print("Okrenuta matrica: ")
# for red in matrica:
#   for el in red:
#     print(el, end=" ")
#   print()

######################################

def parnost(torke):
  parne = []
  neparne = []

  for torka in torke:
    if sum(torka) % 2 == 0:
      parne.append(torka)
    else:
      neparne.append(torka)

  return parne, neparne

torke = []
n = int(input("Unesi broj torki: "))

for i in range(n):
  while True:
    element = input("Unesi elemente torke odvojene razmakom: ").split()
    if len(element) == 3:
      torka = tuple(map(int, element))
      torke.append(torka)
      break
    else:
      print("Torka mora imati tacno 3 elementa!")

parneTorke, neparneTorke = parnost(torke)

print(f"Sve torke zajendo {torke}")
print(f"Parne torke: {parneTorke}")
print(f"Neparne torke: {neparneTorke}")