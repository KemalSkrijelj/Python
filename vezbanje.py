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

n = int(input("Unesi n za kvadratnu jednacinu: "))
while n <= 1 or n >= 10:
  n = int(input("Unesi n u opsegu od 1 do 10: "))

matrica = []

print("Unesi matricu: ")
for i in range(n):
  red = []
  for j in range(n):
    element = int(input(f"Unesi element [{i}][{j}]: "))
    red.append(element)
  matrica.append(red)

print("Prikaz matrice: ")
for red in matrica:
  for el in red:
    print(el, end = " ")
  print()

print("Nova matrica: ")
for i in range(n):
  for j in range(i, n):
    matrica[i][j], matrica[j][i] = matrica[j][i], matrica[i][j]
  
for i in range(n):
  matrica[i].reverse()

print("Prikaz matrice: ")
for red in matrica:
  for el in red:
    print(el, end = " ")
  print()
