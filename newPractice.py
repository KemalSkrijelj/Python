import math

# def pomerajListe(lista, k, pravacRotacije):
#   if pravacRotacije == "levo":
#     k = k % len(lista)
#     return  lista[k:] + lista[:k]
#   elif pravacRotacije == "desno":
#     k = k % len(lista)
#     return lista[-k:] + lista[:-k]
#   else:
#     print("Pravac mora biti il levo ili desno!")
#     return lista
# lista = []
# k = int(input("Unesi broj pomeraja: "))
# pravacRotacije = input("Unesi pravac rotacije: ")
# n = int(input("Unesi broj el liste: "))
# for i in range(n):
#   el = int(input("Unesi el liste: "))
#   lista.append(el)

# pomerenaLista = pomerajListe(lista, k, pravacRotacije)
# print(f"Pomerena lista: {pomerenaLista}")

################################
# def izbacivanjeEl(lista):
#   najveci = max(lista)
#   najmanji = min(lista)

#   while najveci in lista:
#     pozicija = lista.index(najveci) + 1
#     print(f"Izbacen je najveci el:{najveci}, pozicija: {pozicija}")
#     lista.remove(najveci)

#   if najmanji in lista:
#     prviMin = lista.index(najmanji)+1
#     print(f"Izbacen prvi najmanji el:{najmanji}, pozicija: {prviMin}")
#     lista.pop(najmanji)
#   if najmanji in lista:
#     poslednjiMin = len(lista)-1-lista[::-1].index(najmanji)
#     print(f"Poslednji najmanji el: {najmanji}, pozicija: {poslednjiMin}")
#     lista.pop(najmanji)

# lista = []
# n = int(input("Unesi duzinu liste: "))
# for i in range(n):
#   el = int(input("Unesi el liste: "))
#   lista.append(el)
# izbacivanjeEl(lista)

################################

# def artSredina(lista,n):
#   for i in range(1, n - 1):
#     if lista[i] == (lista[i-1]+lista[i+1])/2:
#       print(f"Element na indeksu {i} ispunjava uslov")
      
# n = int(input("Unesi duzinu niza: "))
# while n < 3 or n > 100:
#   n = int(input("Unesi duzinu niza(3-100): "))

# lista = []

# for _ in range(n):
#   el = int(input("Unesi el liste: "))
#   lista.append(el)

# artSredina(lista,n)

################################
# def toDecimal(listaKaraktera):
#   return int("".join(listaKaraktera), 16)

# listaKaraktera = []
# for i in range(6):
#   karakteri = "0123456789ABCDEF"
#   el = input("Unesi karaktere(0-9)(A-F): ").upper()
#   if el not in karakteri:
#     print("Uneli ste nedozvoljen karakter")
#     break
#   else:
#     listaKaraktera.append(el)

# decimalanBroj = toDecimal(listaKaraktera)
# print(f"Uneti niz karaktera u decimalnom zapisu je: {decimalanBroj}")

################################

# dozvoljeniBrojevi = [1,2,5,10,20]
# matrica = []
# n = int(input("Unesi red: "))
# m = int(input("Unesi kolonu: "))
# for i in range(n):
#   red = []
#   for j in range(m):
#     while True:
#       el = int(input("Unesi el matrice(1,2,5,10,20): "))
#       if el in dozvoljeniBrojevi:
#         red.append(el)
#         break
#       else:
#         print("Uneli ste nedozvoljen broj")
#   matrica.append(red)

# print("Matrica: ")
# for red in matrica:
#   for el in red:
#     print(el, end=" ")
#   print()

# sumaGlavne = 0
# for i in range(min(n,m)):
#       sumaGlavne += matrica[i][i]

# for i in range(n):
#   for j in range(m): 
#     if i == j:
#       sumaGlavne += matrica[i][j]

# najmanjiEl = float('inf')
# for i in range(n):
#   for j in range(m):
#     if i < j:
#       if matrica[i][j] < najmanjiEl:
#         najmanjiEl = matrica[i][j]

# print(f"Najmanji el je {najmanjiEl}.")
# print(f"Suma el glavne dijagonale je: {sumaGlavne}")

################################
# def parne(torke):
#   parneTorke = []
#   for torka in torke:
#     if all(el% 2 == 0 for el in torka):
#       parneTorke.append(torka)
#   return parneTorke
# torke = []
# n = int(input("Unesi broj torki: "))
# for i in range(n):
#   torka = tuple(map(int, input(f"Unesi el {i+1}torke, odvojene razmakom: ").split()))
#   torke.append(torka)

# najvecaTorka = torke[0]
# for torka in torke:
#   if sum(torka) > sum(najvecaTorka):
#     najvecaTorka = torka

# print(f"Torka s najvecom sumom je: {najvecaTorka}")

# parneTorke = parne(torke)
# print(f"Parne torke: {parneTorke}")

# sortiranaTorka = sorted(torke, key=lambda x : x[1], reverse=True)
# print(f"Sortirana torka: {sortiranaTorka}")

################################

torke = []
n = int(input("Unesi broj torki: "))

for i in range(n):
  torka = tuple(map(float, input("Unesi elemente torke(odvojene razmakom): ").split()))
  while len(torka) != 3:
    torka = tuple(map(float, input("Torka sme imati 3 elementa: ").split()))
  torke.append(torka)

sortiraneTorke = sorted(torke, key=lambda torka : sum(torka) / len(torka))

for torka in torke:
  prosek = sum(torka) / len(torka)
  print(f"Torka: {torka} s prosekom: {prosek}")

print(f"Sortirane torke: {sortiraneTorke}")