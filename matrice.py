import math as math


# niz = [1,2,5,10,20]
# n = int(input("Unesi n kao vrstu i kolonu kod matrica: "))
# matrica = []
# for i in range(n):
#   red = []
#   for j in range(n):
#     el = int(input(f"Unesi kovanicu(1,2,5,10,20) u matrici[{i}][{j}]: "))
#     while el not in niz:
#       el = int(input(f"Unesi dozvoljene kovanice(1,2,5,10,20) u matrici[{i}][{j}]: "))
#     red.append(el)
#   matrica.append(red)

# for red in matrica:
#   for el in red:
#     print(el, end=" ")
#   print()

# sumaEl = 0
# for i in range(n):
#   for j in range(n):
#     if i==j:
#       sumaEl += matrica[i][j]
# print(f"Suma elemenata na glavnoj dijagonali je {sumaEl}")

# minEl = float('inf')
# for i in range(n):
#   for j in range(n):
#     if i < j:
#       if matrica[i][j]< minEl:
#         minEl = matrica[i][j]

# print(f"Najmanji element iznad glavne dijagonale je {minEl}")

#####################################

# n = int(input("Unesi broj vrsti matrice: "))
# m = int(input("Unesi broj kolona matrice: "))
# matrica = []

# minEl = float('inf')
# maxEl = float('-inf')
# najvecaVrsta = -1
# najmanjaVrsta = -1

# for i in range(n):
#   red = []
#   for j in range(m):
#     el = int(input(f"Unesi el matrice[{i}][{j}]: "))
#     red.append(el)
#   matrica.append(red)

# print("Matrica: ")
# for red in matrica:
#   for el in red:
#     print(el,end=" ")
#   print()

# for i in range(n):
#   for j in range(m):
#     if matrica[i][j]< minEl:
#       minEl = matrica[i][j]
#       najmanjaVrsta = i
#     if matrica[i][j]> maxEl:
#       maxEl = matrica[i][j]
#       najvecaVrsta = i

# matrica[najmanjaVrsta], matrica[najvecaVrsta] = matrica[najvecaVrsta], matrica[najmanjaVrsta]

# print("Nova matrica: ")
# for red in matrica:
#   for el in red:
#     print(el,end=" ")
#   print()

#####################################

# n = int(input("Unesi n za kvadratnu matricu: "))
# matrica = []
# sumEl = 0
# for i in range(n):
#   red = []
#   for j in range(n):
#     el = int(input(f"Unesi el matrice[{i}][{j}]: "))
#     red.append(el)
#   matrica.append(red)

# print("Matrica: ")
# for red in matrica:
#   for el in red:
#     print(el,end=" ")
#   print()

# for i in range(n):
#   for j in range(n):
#     if j == n-1-i:
#       sumEl += matrica[i][j]
# print(f"Suma el sporedne dijagonale {sumEl}")

# maxEl = float('-inf')

# for i in range(n):
#   for j in range(n):
#     if j < n-1-i:
#       if matrica[i][j] > maxEl:
#         maxEl = matrica[i][j]

# print(f"Najveci el iznad sporedne dijagonale {maxEl}")

#####################################

# n = int(input("Unesi n za kvadratnu matricu: "))
# while n < 1 or n > 10:
#   n = int(input("N mora biti u opsegu od 1 do 10: "))

# matrica = []
# sumEl = 0
# for i in range(n):
#   red = []
#   for j in range(n):
#     el = int(input(f"Unesi el matrice[{i}][{j}]: "))
#     red.append(el)
#   matrica.append(red)

# print("Matrica: ")
# for red in matrica:
#   for el in red:
#     print(el,end=" ")
#   print()

# for i in range(n):
#   for j in range(i,n):
#     matrica[i][j], matrica[j][i] = matrica[j][i], matrica[i][j]

# for i in range(n):
#   matrica[i].reverse()

# print("Matrica okrenuta za 90stepeni: ")
# for red in matrica:
#   for el in red:
#     print(el,end=" ")
#   print()

#####################################

# n = int(input("Unesi n za kvadratnu matricu: "))

# matrica = []
# sumEl = 0
# for i in range(n):
#   red = []
#   for j in range(n):
#     el = int(input(f"Unesi el matrice[{i}][{j}]: "))
#     red.append(el)
#   matrica.append(red)

# print("Matrica: ")
# for red in matrica:
#   for el in red:
#     print(el,end=" ")
#   print()

# for i in range(n):
#   for j in range(i,n):
#     matrica[i][j], matrica[j][i] = matrica[j][i], matrica[i][j]

# print("Transponovana matrica: ")
# for red in matrica:
#   for el in red:
#     print(el,end=" ")
#   print()

#####################################

# n = int(input("Unesi broj vrsti matrice: "))
# m = int(input("Unesi broj kolona matrice: "))
# while n < 1 :
#   n = int(input("N mora biti veci od 1 "))
# while m>10:
#   m = int(input("M mora biti manji od 10: "))
  


# matrica = []
# sumEl = 0
# for i in range(n):
#   red = []
#   for j in range(m):
#     el = int(input(f"Unesi el matrice[{i}][{j}]: "))
#     red.append(el)
#   matrica.append(red)

# print("Matrica: ")
# for red in matrica:
#   for el in red:
#     print(el,end=" ")
#   print()

# sedlasteTacke = []

# for i in range(n):
#   minEl = min(matrica[i])
#   minIndex = matrica[i].index(minEl)

#   isBiggest = True

#   for j in range(m):
#     if matrica[j][minIndex]> minEl:
#       isBiggest = False
#       break
#   if isBiggest:
#     sedlasteTacke.append((i,minIndex))

# if sedlasteTacke:
#   print("Sedlaste tacke: ")
#   for tacka in sedlasteTacke:
#     print(f"Red: {tacka[0]}, kolona: {tacka[1]}")
# else:
#   print("Nema sedlastih tacki")

#####################################

n = int(input("Unesi broj vrsti matrice: "))
m = int(input("Unesi broj kolona matrice: "))
matrica = []
for i in range(n):
  red = []
  for j in range(m):
    el = int(input(f"Unesi el matrice[{i}][{j}]: "))
    red.append(el)
  matrica.append(red)

print("Matrica: ")
for red in matrica:
  for el in red:
    print(el, end=" ")
  print()

sumaSporedne = 0
for i in range(n):
  for j in range(m):
    if j == n-1-i:
      sumaSporedne += matrica[i][j]
sumaIznadSporedne = 0
for i in range(n):
  for j in range(m):
    if j < n-1-i:
      sumaIznadSporedne += matrica[i][j]

print(f"Suma el. sporedne dijagonale: {sumaSporedne}")
print(f"Suma el. iznad sporedne dijagonale: {sumaIznadSporedne}")