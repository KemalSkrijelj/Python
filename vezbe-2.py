import random
from collections import Counter
# recenica = "Kemal se preziva SKrijelj, student"
# print(recenica.strip()) #ova strip funkcija se koristi da makne prazan prostor
# print(recenica.lower())
# print(recenica.upper())
# print(recenica.replace("K", "S")) #menja karakter K sa karakterom S
# print(recenica.replace("Kemal", "K")) #menja rec Kemal sa karakterom K
# print(recenica.split(",")) #Razdvaja recenicu na delove, gde god ima ,
# print(recenica.split(" ")) #Razdvaja recenicu na delove, gde god ima space
# voce = list(("Banana","Jabuka","Kiwi")) #ovo list(()) sluzi da napravi listu
# print(voce)
# nekoVoce = ["Jabuka", "Banana","Ananas","Lubenica"]
# nekoVoce.insert(1,"Pomorandza")# sluzi da na poziciji 1 ubacimo element Pomorandza a da nikog ne makne iz liste
# print(nekoVoce)

# del nekoVoce[2] #brise element iz liste
# del nekoVoce #brise celu listu, ne postoji vise
# nekoVoce.remove("Ananas") #brise konkretnu stvar 
# nekoVoce.pop() #uklanja zadnji element iz liste
# print(nekoVoce)
###################################

# zamisljenBroj = random.randint(1,100)
# print(zamisljenBroj)

# ime = input("Unesi svoje ime: ")
# print("Zapoceli ste igru!")

# print("Pogodi broj koji je zamisljen: \n")


# while True:
#   unos = int(input("Unesi broj: \n"))

#   if unos < zamisljenBroj:
#     print("Uneti broj je manji od zamisljenog")
#   elif unos > zamisljenBroj:
#     print("Uneti broj je veci od zamisljenog")
#   else:
#     print(f"Pogodili ste broj, to je broj {unos}")
#     break

###################################
 
# lista = []

# n = int(input("Unesi duzinu liste"))
# s = 0
# for i in range(n):
#   el = int(input("Unesi element"))
#   lista.append(el)
#   s += el

# prosek = s / n
# print(f"Prosek liste je {prosek}")

###################################
# def jedanDeljiv(lista, k):
#   for element in lista:
#     if element % k == 0:
#       print("Deljiv je najmanje jedan element iz liste")
#       return True

# def sviDeljivi(lista,k):
#   for i in lista:
#     if lista[i] % k != 0:
#       print("Nisu svi elementi deljivi")
#       return False
#   return True  

# lista = []
# k = int(input("Unesi kolicnik: "))
# n = int(input("Unesi duzinu liste"))
# print("Unesi elemente liste: \n")
# for i in range(n):
#   element= int(input("Unesi elemente liste: \n"))
#   lista.append(element)

# print(lista)

# jedanDeljiv(lista,k)
# sviDeljivi(lista,k)
###################################

# def pomeraj(lista, k, pravac):
#   if pravac == "desno":
#     return lista[-k:] + lista[:-k]
#   else:
#     return lista[k:] +lista[:k]
# lista = []
# k = int(input("Unesi broj rotacije: "))
# n = int(input("Unesi duzinu liste: "))
# pravac = str(input("U koju stranu se pomera lista (levo ili desno): "))

# print("Unesi elemente liste: ")
# for i in range(n):
#   el = input("Unesi element: ")
#   lista.append(el)

# novaLista = pomeraj(lista,k,pravac)
# print(f"Lista koja je obrnuta kako ste zeleli je {novaLista}")
###################################
# def drugiPoVelicini(lista):
#   lista.sort(reverse = True)

#   max1 = lista[0] 
#   max2 = lista[1]

#   for broj in lista[2:]:
#     if broj < max1 and broj != max2:
#       max2 = broj
#       break

#   return max2


# n = int(input("Unesi duzinu liste: "))
# lista = []
# print("Unesi elemente liste: ")
# for i in range(n):
#   el = input()
#   lista.append(el)
 
# drugi = drugiPoVelicini(lista)

# print(f"Drugi po velicini broj u lisit je {drugi}")
###################################
# def binomniKoef(n, k):
#   if k == 0 or k == n:
#     return 1
  
#   return binomniKoef(n-1,k-1)+ binomniKoef(n-1,k)

# n = int(input("Unesi n: "))
# k = int(input("Unesi k: "))

# if k > n:
#   print("K ne moze biti vece od n")
# else:
#   print(f"Rezultat je: {binomniKoef(n,k)}")
###################################

# lista = []
# n = int(input("Unesi duzinu liste: "))
# print("Unesi elemente liste: ")
# for i in range(n):
#   el = int(input())
#   lista.append(el)

# maxElement = max(lista)

# for i in lista[:]:
#   if i == maxElement:
#     pozicija = lista.index(i)
#     print(f"Izbacen je element s pozicije {i+1}")
#     lista.remove(i)
  
# minElement = min(lista)

# for i in lista:
#   if i == minElement:
#     pozicija = lista.index(i) #SLUZI ZA UZIMANJE POZICIJE TOG ELEMENTA na poziciji i
#     print(f"Izbacen je element s pozicije {i+1}")
#     lista.remove(i)
#     break

# minElement = min(lista)

# for i in lista[::-1]:
#   if i == minElement:
#     pozicija = lista.index(i)
#     print(f"Izbacen je element s pozicije {i+1}")
#     lista.remove(i)
#     break

###################################
# def prosecnaTemp(s, days):
#   return s / days
# def najvecaTemp(lista):
#   maxTemp = max(lista)
#   indeks = lista.index(maxTemp)
#   return print(f"Najveca temperatura {maxTemp}, dan: {indeks+1}")
# def najmanjaTemp(lista):
#   minTemp = min(lista)
#   indeks = lista.index(minTemp)
#   return print(f"Najmanja temperatura {minTemp}, dan: {indeks+1}")
  
# lista = []
# days = 7
# print("Unesi temperaturu svakog dana u nedelji")
# s = 0

# for i in range(days):
#   temp = int(input())
#   lista.append(temp)
#   s += temp

# prosek = prosecnaTemp(s,days)
# minTemp = najmanjaTemp(lista)
# maxTemp = najvecaTemp(lista)

# print(f"Prosecna temperatura temp {prosek}")
###################################
# def samoSamoglasnici(listaReci):
#   samoglasnici = "aeiouAEIOU"
#   return [rec for rec in listaReci if all(char in samoglasnici for char in rec)]

# def istiPocetakiKraj(listaReci):
#   return [rec for rec in listaReci if rec[0].lower() == rec[-1].lower()]

# def poDuzini(listaReci):
#   return sorted(listaReci, key=len)

# listaReci = []
# print("Unesi reci: ")
# duzinaListe = int(input("Unesi broj za duzinu niza: "))

# for _ in range(duzinaListe):
#   rec = str(input("Unesi rec: "))
#   listaReci.append(rec)

# reciSamoglasnici = samoSamoglasnici(listaReci)
# slicni = istiPocetakiKraj(listaReci)
# sortirani = poDuzini(listaReci)

# print(f"Reci koje imaju samo samoglasnike {reciSamoglasnici}")
# print(f"Reci iste na pocetku i kraju {slicni}")
# print(f"Sortirana lista po duzini reci {sortirani}")
###################################
# def brojPonavljanja(listaReci):
#   brojReci = {}
#   for rec in listaReci:
#     if rec in brojReci:
#       brojReci[rec] += 1
#     else:
#       brojReci[rec] = 1
#   return brojReci

# def najduzaRec(listaReci):
#   najduza = ""
#   for rec in listaReci:
#     if len(rec) > len(najduza):
#       najduza = rec 
#   return najduza

# def palindrom(listaReci):
#   palindromi = []
#   for rec in listaReci:
#     if rec == rec[::-1]:
#       palindromi.append(rec)
#   return palindromi


# listaReci = []
# print("Unesi reci: ")
# duzinaListe = int(input("Unesi broj za duzinu niza: "))

# for _ in range(duzinaListe):
#   rec = input("Unesi rec odvojene razmakom: ")
#   listaReci.append(rec)

# palin = palindrom(listaReci)
# if palin:
#   print(f"Palindromi: {','.join(palin)}")
# else:
#   print("Nema palindroma")

# najduza = najduzaRec(listaReci)
# print(f"Najduza rec {najduza}")

# ponavljanja = brojPonavljanja(listaReci)
# print(f"Reci koje se ponavljaju: {ponavljanja}")
###################################
# zamisljeniBroj = random.randint(1,100)

# ime = input("Unesi svoje ime")

# while True:
#   unos = int(input("Unesi broj"))
#   if unos > zamisljeniBroj:
#     print("Uneti broj je veci od zamisljenog")
#   elif unos < zamisljeniBroj:
#     print("Uneti broj je manji od zamisljenog")
#   else:
#     print(f"Pogodili ste broj to je {zamisljeniBroj}")
#     break

###################################
# def prosek(n, s):
#   return s / n

# lista = []
# s = 0
# n = int(input("Unesi n duzinu liste: "))
# for _ in range(n):
#   element = int(input("Unesi el: "))
#   lista.append(element)
#   s += element

# prosecnaVrednost = prosek(n,s)
# print(f"Prosecna vrednost {prosecnaVrednost}")
# for i in range(n):
#   if lista[i] > prosek(n,s):
#     print(f"Element veci od proseka: {lista[i]}")
###################################
# def pomerajListe(lista,k,pravac):
#   if pravac == "desno":
#     return lista[-k:] + lista[:-k]
#   else:
#     return lista[k:] + lista[:k]

# lista = []
# n = int(input("Unesi n duzinu liste: "))
# k = int(input("Unesi za koliko pozicija da se pomera: "))
# pravac = str(input("Unesi pravac(desno ili levo): "))
# for _ in range(n):
#   element = int(input("Unesi el: "))
#   lista.append(element)

# novaLista = pomerajListe(lista,k,pravac)
# print(f"Nova lista: {novaLista}")
###################################
# def drugaPoVelicini(lista):
#   lista.sort(reverse = True)
  
#   max1 = lista[0]
#   for broj in lista[1:]:
#     if broj != max1:  
#       return broj 
    
# lista = []
# n = int(input("Unesi n duzinu liste: "))
# for _ in range(n):
#   element = int(input("Unesi el: "))
#   lista.append(element)

# drugi = drugaPoVelicini(lista)
# print(f"Drugi po velicini je broj {drugi}")
###################################
# def binomniKoeficijent(n,k):
#   if k == 0 or k == n:
#     return 1
#   return binomniKoeficijent(n-1,k-1) + binomniKoeficijent(n-1,k) 
  
# n = int(input("Unesi n: "))
# k = int(input("Unesi k: "))
# binom = binomniKoeficijent(n,k)
# print(f"Binomni koeficijent: {binom}")
###########################################
# lista = []
# n = int(input("Unesi n duzinu liste: "))
# for _ in range(n):
#   element = int(input("Unesi el: "))
#   lista.append(element)
# print(f"Lista je duzine {n} i elementi su: {lista}")

# maxElement = max(lista)

# for el in lista[:]:
#   if el == maxElement:
#     pozicija = lista.index(el)
#     print(f"Izbacen je broj {el} na poziciji {pozicija + 1}")
#     lista.remove(el)

# minElement = min(lista)

# for el in lista:
#   if el == minElement:
#     pozicija = lista.index(el)
#     print(f"Izbacen je broj {el} na poziciji {pozicija + 1}")
#     lista.remove(el)
#     break

# minElement = min(lista)

# for el in lista[::-1]:
#   if el == minElement:
#     pozicija = lista.index(el)
#     print(f"Izbacen je element {el} na poziciji {pozicija + 1}")
#     lista.remove(el)
#     break
###########################################
# def prosekTemp(s, days):
#   return s / days

# lista = []
# days = 7
# s = 0
# for i in range(days):
#   element = int(input(f"Unesi temperaturu za dan-{i+1}: "))
#   lista.append(element)
#   s+=element

# print(lista)

# maxTemp = lista[0]
# minTemp = lista[0]
# pozicijaMin = 0
# pozicijaMax = 0
# for i in range(1, len(lista)):
#   if lista[i] > maxTemp:
#     maxTemp = lista[i]
#     pozicijaMax = i
#   if lista[i] < minTemp:
#     minTemp = lista[i]
#     pozicijaMin = i

# prosecnaTemperatura = prosekTemp(s,days)
# print(f"Max temp je {maxTemp} ,dan: {pozicijaMax + 1}")
# print(f"Min temp je {minTemp} ,dan: {pozicijaMin + 1}")
# print(f"Prosecna temperatura je {prosecnaTemperatura}")
###########################################
# def samoglasnci(lista):
#   samoglasnik = "aeiouAEIOU"
#   return [rec for rec in lista if all(char in samoglasnik for char in rec)]

# def slicne(lista):
#   reciIste = []
#   for i in range(len(lista)):
#    if lista[i][0] == lista[i][-1]:
#     reciIste.append(lista[i])
#   return reciIste
# def sortirane(lista):
#   lista.sort(key = len)
#   return lista

# lista = []
# n = int(input("Unesi n: "))
# for i in range(n):
#   element = input("Unesi rec: ")
#   lista.append(element)

# reciSamoglasnici = samoglasnci(lista)
# isteReci = slicne(lista)
# sortirana = sortirane(lista)

# print(f"Reci sa samoglasnicima: {reciSamoglasnici}")
# print(f"Reci sa istim slovom na pocetak i na kraj: {isteReci}")
# print(f"Sortiran niz po duzini: {sortirana}")
###########################################
# def ponavljanjeReci(lista):
#   brojPonavljanja = {}

#   for rec in lista:
#     if rec in brojPonavljanja:
#       brojPonavljanja[rec] += 1
#     else:
#       brojPonavljanja[rec] = 1

#     reciPonavljanje = {}
#     for rec, broj in brojPonavljanja.items():
#       if broj > 1:
#         reciPonavljanje[rec] = broj

#   return reciPonavljanje

# def najduzaRec(lista):
#   najduza = lista[0]
#   for rec in lista:
#     if len(rec) > len(najduza):
#       najduza = rec
#   return najduza

# def palindrom(lista):
#   palindromi = []
#   for rec in lista:
#     if rec == rec[::-1]:
#       palindromi.append(rec)
#   return palindromi

# lista = []
# n = int(input("Unesi n: "))
# for i in range(n):
#   element = input("Unesi rec: ")
#   lista.append(element)

# palindromi = palindrom(lista)
# najduza = najduzaRec(lista)
# ponavljanje = ponavljanjeReci(lista)

# print(f"Reci koje su palindromi: {palindromi}")
# print(f"Najduza rec: {najduza}")
# print(f"Reci koje su ponavljaju: {ponavljanje}")
###########################################
