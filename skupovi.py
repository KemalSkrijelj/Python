import math as math
import string

# torka = (1,2,3)
# skup = set(torka)
# print(torka)
# print(skup)

###########################
# def a(lista1,lista2):
#   s1, s2 = set(lista1), set(lista2)
#   return s1 & s2

# def b(*lista1):
#   sets = [set(l) for l in lista1]
#   return set.intersection(*sets)
# lista1 = [1,2,3]
# lista2 = [3,4,5]

###########################

# n = int(input("Unesi duzinu nekog skupa: "))
# skup = set()
# toRemove = set()

# for i in range(n):
#   el = int(input("Unesi element: "))
#   skup.add(el)

# print(skup)

# for el in skup:
#   if el % 2 == 0:
#     print(f"Parni el u skupu: {el}")
#     toRemove.add(el)

# for el in toRemove:
#   skup.remove(el)

# print(skup)

###########################

# def isHeterogram(recenica):
#   ponovljenaSlova = set()
#   for char in recenica:
#     if char.isalpha():
#       char = char.lower()
#       if char in ponovljenaSlova:
#         return False
#       ponovljenaSlova.add(char)
#   return True

# recenica = input("Unesi recenicu: ")

# if isHeterogram(recenica):
#   print("Recenica je heterogram")
# else:
#   print("Recenica nije heterogram")

###########################

# def isPangram(recenica):
#   abeceda = string.ascii_lowercase
#   recenicaSet = set()
#   for char in recenica:
#     if char.isalpha():
#         recenicaSet.add(char.lower())
  
#   return recenicaSet >= set(abeceda)

# recenica = input("Unesi recenicu: ")

# if isPangram(recenica):
#   print("Recenica je pangram")
# else:
#   print("Recenica nije pangram")

###########################
# def presek(lista,lista2):
#   lista, lista2 = set(lista), set(lista2)
#   return lista & lista2

# def unija(lista,lista2, lista3):
#   lista, lista2, lista3 = set(lista), set(lista2), set(lista3)
#   return lista.intersection(lista2,lista3)
# def jedno(lista,lista2, lista3):
#   lista, lista2, lista3 = set(lista), set(lista2), set(lista3)
#   return lista ^ lista2 ^ lista3


# lista = [8,3,5,6,7]
# lista2 = [9,0,3,8,7]
# lista3 = [0,3,2,1,5]

# presekSkupova = presek(lista,lista2)
# print(f"Presek skupova {presekSkupova}")
# unijaSkupova = unija(lista,lista2,lista3)
# print(f"Unija skupova {unijaSkupova}")

# samoUJednoj = jedno(lista,lista2,lista3)
# print(f"U jednom od skupova {samoUJednoj}")

###########################

# def isHeterogram(recenica):
#   ponavljanje = set()
#   for char in recenica:
#     if char.isalpha():
#       char = char.lower()
#       if char in ponavljanje:
#         return False
#       ponavljanje.add(char)
#   return True

# recenica = input("Unesi recenicu: ")

# if isHeterogram(recenica):
#   print("Recenica je heterogram")
# else:
#   print("Recenica nije heterogram")

###########################

# def isPangram(recenica):
#   abeceda = set('abcdefghijklmnopqrstuvwxyz')
#   recenicaSet = set()
#   for char in recenica:
#     if char in abeceda:
#       recenicaSet.add(char.lower())
#   return recenicaSet >= abeceda

# recenica = input("Unesi recenicu: ")

# if isPangram(recenica):
#   print("Recenica je parangram")
# else:
#   print("Recenica nije parangram")

###########################

# def isHeterogram(recenica):
#   ponavljanjeSlova = set()
#   for char in recenica:
#     if char.isalpha():
#       char = char.lower()
#       if char in ponavljanjeSlova:
#         return False
#   return True

# recenica = input("Unesi recenicu: ")

# if isHeterogram(recenica):
#   print("Recenica je heterogram")
# else:
#   print("Recenica nije heterogram")

###########################

# def presekElementa(l1,l2):
#   l1,l2 = set(l1), set(l2)
#   return l1 & l2
# def zajednickiEl(l1,l2,l3):
#   l1,l2, l3 = set(l1), set(l2), set(l3)
#   return l1.intersection(l2,l3)
# def uJednojListi(l1,l2,l3):
#   l1,l2, l3 = set(l1), set(l2), set(l3)
#   return (l1 - l2-l3) | (l2 - l1-l3) | (l3 - l2-l1)

# l1, l2, l3 = [8, 3, 5, 6, 7], [9, 0, 3, 8, 7], [0, 3, 2,1,5]

# presekSkupova = presekElementa(l1,l2)
# print(f"Presek skupova {presekSkupova}")
# unijaSkupova = zajednickiEl(l1,l2,l3)
# print(f"Unija skupova {unijaSkupova}")

# samoUJednoj = uJednojListi(l1,l2,l3)
# print(f"U jednom od skupova {samoUJednoj}")

###########################

def isParangram(recenica):
  abeceda = set('abcdefghijklmnopqrstuvwxyz')
  recenicaSet = set()
  for char in recenica:
    if char in abeceda:
      recenicaSet.add(char.lower())
  return recenicaSet >= abeceda

recenica = input("Unesi recenicu: ")

if isParangram(recenica):
  print("Recenica je parangram")
else:
  print("Recenica nije parangram")
