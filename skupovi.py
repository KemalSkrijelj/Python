import math as math
import string
from collections import Counter
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

# def isParangram(recenica):
#   abeceda = set('abcdefghijklmnopqrstuvwxyz')
#   recenicaSet = set()
#   for char in recenica:
#     if char in abeceda:
#       recenicaSet.add(char.lower())
#   return recenicaSet >= abeceda

# recenica = input("Unesi recenicu: ")

# if isParangram(recenica):
#   print("Recenica je parangram")
# else:
#   print("Recenica nije parangram")

###########################
# def isHeterogram(recenica):
#   ponovljenoSlovo = set()
#   for char in recenica:
#     if char.isalpha():
#       char = char.lower()
#       if char in ponovljenoSlovo:
#         return False
#       ponovljenoSlovo.add(char)
#   return True

# recenica = input("Unesi recenicu: ") 
# if isHeterogram(recenica):
#   print("Recenica je heterogram. ")
# else:
#   print("Recenica nije heterogram. ") 

###########################
# def isPangram(recenica):
#   abeceda = set('abcdefghijklmnopqrstzwxyz')
#   recenicaNova = set()
#   for char in recenica:
#     if char in abeceda:
#       recenicaNova.add(char.lower())
#   return recenicaNova >= abeceda

# recenica = input("Unesi recenicu: ")

# if isPangram(recenica):
#   print("Recenica je pangram")
# else:
#   print("Recenica nije pangram")
###########################

# def skupovi():
#   prviSkup = set(map(int, input("Unesi elemente prvog skupa(odvojene zarezom)").split(',') ))
#   drugiSkup = set(map(int, input("Unesi elemente drugog skupa(odvojene zarezom)").split(',') ))

#   if prviSkup <= drugiSkup:
#     print("Prvi skup je podskup drugog.")
#   else:
#     print("Prvi skup nije podskup drugog.")

#   unija = prviSkup | drugiSkup
#   presek = prviSkup & drugiSkup

#   print(f"Unija skupova {unija}")
#   print(f"Presek skupova {presek}")

# skupovi()
###########################

# lista = []
# n = int(input("Unesi duzinu niza: "))
# for i in range(n):
#   el = int(input("Unesi elemente niza: "))
#   lista.append(el)

# print(f"Uneta lista: {lista}")

# skup = set(lista)
# print(f"Skup od unete liste: {skup}")
# listaBezDuplikata = list(skup)
# print(f"Lista bez duplikata: {listaBezDuplikata}")
###########################

# skup2 = {"level", "python", "c", "javascript"}
# skup = {"level", "python", "radar", "hello"}
# niz = [1,2,2,3,4,4,5]

# def najcesciElementi(niz):
#   vidjeni = []
#   ponovljeni = []
#   for el in niz:
#     if el in vidjeni:
#       ponovljeni.append(el)
#     else:
#       vidjeni.append(el)
#   print(f"Ponovljeni brojevi: {set(ponovljeni)}")

# najcesciElementi(niz)
# def razlikaSkupova(skup,skup2):
#   razlika = skup - skup2
#   print(f"Razlika kod skupova: {razlika}")
  
# razlikaSkupova(skup,skup2)

# def isPalindrom(skup):
#   lista = list(skup)
#   palindromi = []
#   for rec in lista:
#     if rec[:] == rec[::-1]:
#       palindromi.append(rec)
#   print(f"Skup palindroma je: {set(palindromi)}")
# isPalindrom(skup)

# simetricaRazlika = skup ^ skup2
# print(f"Simetricna razlika {simetricaRazlika}")

###########################
# def zajednickiElUSkupovima(skupovi, n):
#   zajednicki = skupovi[0]
#   for i in range(1,n):
#     noviZajednicki = []
#     for el in zajednicki:
#       if el in skupovi[i]:
#         noviZajednicki.append(el)
#     zajednicki = noviZajednicki
#     return zajednicki
  
#   return set(zajednicki)
# n = int(input("Unesi broj skupova"))
# skupovi = []

# for i in range(n):
#   skup = set(map(int, input(f"Unesi elemente {i+1} skupa(odvojeni zarezom): ").split(',') ))
#   skupovi.append(skup)

# rezultat = zajednickiElUSkupovima(skupovi, n)
# print(f"Rezultat: {rezultat}")
# print(skupovi)

###########################
# def zajednickeReci(listaRecenica):
#   reciURecenici = [set(recenica.split()) for recenica in listaRecenica]
#   return set.intersection(*reciURecenici)

# n = int(input("Unesi broj recenica u skupu: "))
# listaRecenica = []
# for i in range(n):
#   skup = input(f"Unesi {i+1}recenicu: ")
#   listaRecenica.append(skup)

# rezultat = zajednickeReci(listaRecenica)
# print(rezultat)

###########################

# n = int(input("Unesi broj el: "))
# brojevi = []
# for _ in range(n):
#   el = int(input("Unesi broj: "))
#   brojevi.append(el)

# if brojevi[:] == brojevi[::-1]:
#     print(f"Skup {set(brojevi)}  je palindorom")
# else:
#     print(f"Skup {set(brojevi)} nije palindorom")

###########################
# def razlikovanjeDuplikata(reci):
#   ponavljanje = []
#   unikate = []
#   for rec in reci:
#     if reci.count(rec) > 1:
#       ponavljanje.append(rec)
#     else:
#       unikate.append(rec)
#   return set(ponavljanje), set(unikate)

# n = int(input("Unesi broj reci: "))
# reci = []
# for _ in range(n):
#   el = input("Unesi reci: ")
#   reci.append(el)

# ponovljneReci, unikatneReci = razlikovanjeDuplikata(reci)

# print(f"Ponovljene reci: {ponovljneReci}, unikatne: {unikatneReci}")

###########################
def najcesceReci(recenice):
  sveReci = []

  for recenica in recenice:
    sveReci.append(recenica.split())
  
  najcesce = set()
  maxBroj = 0
  for rec in sveReci:
    broj = sveReci.count(rec)
    if broj > maxBroj:
      maxBroj = broj
      najcesce.update(rec)
  return najcesce

n = int(input("Unesi broj rečenica: "))
recenice = []
    
for _ in range(n):
  recenica = input("Unesi rečenicu: ")
  recenice.append(recenica)

rezultat = najcesceReci(recenice)
print(f"Najcesce reci: {rezultat}")