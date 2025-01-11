import math
import random

# zamisljenBroj = random.randint(0,100)
# ime = input("Unesi ime: ") 

# while True:
#   unetiBr = int(input("Unesi broj: "))
#   if unetiBr > zamisljenBroj:
#     print("Uneti broj je veci od zamisljenog.")
#   elif unetiBr < zamisljenBroj:
#     print("Uneti broj je manji od zamisljenog.")
#   else:
#     print(f"Pogodili ste broj. To je {zamisljenBroj}")
#     break

##########################################

# lista = []
# n = int(input("Unesi broj el u listi: "))
# for i in range(n):
#   el = int(input("Unesi el liste: "))
#   lista.append(el)

# prosecnaVrednost = sum(lista) / len(lista)

# for i in range(n):
#   if lista[i] > prosecnaVrednost:
#     print(f"El veci od prosecne vrednosti je {lista[i]}")

##########################################
# def jedanDeljiv(lista, k):
#   for i in range(n):
#     if lista[i] % k == 0:
#       return True
#   return False
# def sviDeljivi(lista,k):
#   for i in range(n):
#     if lista[i] % k != 0:
#       return False
#   return True
# lista = []
# n = int(input("Unesi broj el u listi: "))
# k = int(input("Unesi kolicnik: "))
# for i in range(n):
#   el = int(input("Unesi el liste: "))
#   lista.append(el)

# prviRez = jedanDeljiv(lista,k)
# drugiRez = sviDeljivi(lista,k)

# if prviRez:
#   print("Najmanje jedan el je deljiv s kolicnikom")
# else:
#   print("Nema deljivih s kolicnikom")
# if drugiRez:
#   print("Svi su deljivi s kolicnikom")
# else:
#   print("Nisu svi  deljivi s kolicnikom")

##########################################

# def rotirajListu(lista,k, pravacRotacije):
#   if pravacRotacije == "levo":
#     k = k % len(lista)
#     return lista[k:] + lista[:k]
#   elif pravacRotacije == "desno":
#     k = k % len(lista)
#     return lista[-k:] + lista[:-k]
#   else:
#     print("Unesi levo ili desno.")
#     return lista
  
# lista = []

# n = int(input("Unesi broj el u listi: "))
# k = int(input("Unesi kolicnik: "))
# pravacRotacije = input("Unesi pravac rotacije(levo ili desno): ")

# for i in range(n):
#   el = int(input("Unesi el liste: "))
#   lista.append(el)

# rotiranaLista =  rotirajListu(lista,k,pravacRotacije)
# print(f"Rotirana lista {rotiranaLista}")

##########################################

# def drugiPoVelicini(lista):
#   najveci = float('-inf')
#   drugiNajveci = float('-inf')
#   for broj in lista:
#     if broj > najveci:
#       drugiNajveci = najveci
#       najveci = broj
#     elif broj > drugiNajveci and broj != najveci:
#       drugiNajveci = broj
#   return drugiNajveci

# n = int(input("Unesi duzinu liste: "))
# while n < 2:
#   print("Lista mora biti vece od 2 el.")
#   n = int(input("Unesi duzinu liste: "))
  
# lista = []
# for _ in range(n):
#   el = int(input("Unesi el liste: "))
#   lista.append(el)

# rez =drugiPoVelicini(lista)
# print(rez)

##########################################
# def izbacivanjeEl(lista):
#   najveci = max(lista)
#   najmanji = min(lista)

#   while najveci in lista:
#     pozicija = lista.index(najveci) + 1
#     print(f"Najveci el u listi je {najveci} na poziciji {pozicija}")
#     lista.remove(najveci)
  
#   prviMin = lista.index(najmanji) + 1
#   print(f"Najmanji prvi el je {najmanji} pozicija: {prviMin}")
#   lista.remove(najmanji)

#   if najmanji in lista:
#     poslednjiMin = len(lista) - 1 - lista[::-1].index(najmanji) 
#     print(f"Poslednji najmanji el je {poslednjiMin}, pozicija: {pozicija}")
#     lista.remove(poslednjiMin)
# n = int(input("Unesi duzinu liste: "))
  
# lista = []
# for _ in range(n):
#   el = int(input("Unesi el liste: "))
#   lista.append(el)

# izbacivanjeEl(lista)

##########################################

# def binomniKoef(n, k):
#   if n == 0 or n == k:
#     return 1
#   return (binomniKoef(n-1,k-1) + binomniKoef(n-1,k))

# n = int(input("Unesi n: "))
# k = int(input("Unesi k: "))


# if k > n:
#   print("K ne moze biti vece od n")
# else:
#   print(f"Rezultat je: {binomniKoef(n,k)}")

##########################################

# def prosek(listaTemperatura):
#   return sum(listaTemperatura) / len(listaTemperatura)

# def najtoplijiDan(listaTemperatura):
#   najveci = float('-inf')
#   for i in range(len(listaTemperatura)):
#     if listaTemperatura[i] > najveci:
#       najveci = listaTemperatura[i]
#   pozicija = listaTemperatura.index(najveci) + 1
#   return najveci, pozicija

# def najhladnijiDan(listaTemperatura):
#   najmanji = float('inf')
#   for i in range(len(listaTemperatura)):
#     if listaTemperatura[i] < najmanji:
#       najmanji = listaTemperatura[i]
#   pozicija = listaTemperatura.index(najmanji) + 1
#   return najmanji, pozicija

# listaTemperatura = []
# for i in range(7):
#   dan = int(input(f"Unesi temperaturu za {i+1}dan: "))
#   listaTemperatura.append(dan)

# najvecaTemp, pozicijaNajvece = najtoplijiDan(listaTemperatura)
# najmanjaTemp, pozicijaNajmanje = najhladnijiDan(listaTemperatura)

# print(f"Najveca temp: {najvecaTemp}, na pozicji: {pozicijaNajvece}")
# print(f"Najmanja temp: {najmanjaTemp}, na pozicji: {pozicijaNajmanje}")
# print(f"Prosecna temp je: {prosek(listaTemperatura)}")

##########################################

# def samoSamoglasnici(listaReci):
#   samoglasnici = "aeiou"
#   rezultat = []
#   for rec in listaReci:
#     isSamoglasnik = True
#     for slovo in rec:
#       if slovo not in samoglasnici:
#         isSamoglasnik = False
#         break
#     if isSamoglasnik:
#       rezultat.append(rec)
#   return rezultat

# def isti(listaReci):
#   iste = []
#   for i in range(len(listaReci)):
#     if listaReci[i][0] == listaReci[i][-1]:
#       iste.append(listaReci[i])
#   return iste

# def sortiranaLista(listaReci):
#   return sorted(listaReci, key=len)

# listaReci = []
# n = int(input("Unesi broj reci: "))
# for i in range(n):
#   rec = input(f"Unesi {i+1} rec: ")
#   listaReci.append(rec)

# samoglasnici = samoSamoglasnici(listaReci)
# istiPocetak = isti(listaReci)
# sortirana = sortiranaLista(listaReci)

# print(f"Sortirana lista po duzini: {sortirana}")
# print(f"Reci s samo samoglasnicima: {samoglasnici}")
# print(f"Isto slovo na kraj i pocetak reci: {istiPocetak}")

##########################################

# def rotirajListu(lista, k, pravac):
#   if pravac == "levo":
#     k = k % len(lista)
#     return lista[k:] + lista[:k]
#   elif pravac == "desno":
#     k = k % len(lista)
#     return lista[-k:] + lista[:-k]
#   else:
#     print("Pravac mora biti ili levo ili desno.")
#     return lista

# k = int(input("Unesi broj pomeraja: "))
# pravac = input("Unesi pravac(levo ili desno): ")
# lista = []
# n = int(input("Unesi duzinu liste: "))
# for i in range(n):
#   rec = input(f"Unesi {i+1} rec: ")
#   lista.append(rec)

# rezultat = rotirajListu(lista,k, pravac)
# print(f"Rotirana lista: {rezultat}")

##########################################

# n = int(input("Unesi duzinu dva niza: "))
# while n > 200:
#   n = int(input("Unesi duzinu dva niza(n<200): "))
# nizA = []
# nizB = []
# for i in range(n):
#   elA = int(input(f"Unesi {i+1}broj nizaA: "))
#   elB = int(input(f"Unesi {i+1}broj nizaB: "))
#   nizA.append(elA)
#   nizB.append(elB)

# nizC = []

# for i in range(n):
#   nizC.append(max(nizA[i], nizB[i]))

# print(f"Niz A: {nizA}")
# print(f"Niz B: {nizB}")
# print(f"Niz C: {nizC}")

##########################################

# def isPalindrom(listaReci):
#   palindromi = []
#   for rec in listaReci:
#     if rec[:] == rec[::-1]:
#       palindromi.append(rec)
#   return palindromi
# def ponavljanjeReci(listaReci):
#   brojPonavljanja = {}
#   for rec in listaReci:
#     if rec in brojPonavljanja:
#       brojPonavljanja[rec] +=1
#     else:
#       brojPonavljanja[rec] = 1
#   return brojPonavljanja

# def najduzaRec(listaReci):
#   najduza = listaReci[0]
#   for rec in listaReci:
#     if len(rec) > len(najduza):
#       najduza = rec
#   return najduza

# unos = input("Unesi reci odvojene razmakom: ")
# listaReci = unos.split()

# palindromi = isPalindrom(listaReci)
# brojPonavljanja = ponavljanjeReci(listaReci)
# najduza = najduzaRec(listaReci)

# print(f"Palindromi: {palindromi}")
# print(f"Broj ponavljanje svake reci: {brojPonavljanja}")
# print(f"Najduza rec: {najduza}")

##########################################

# n = int(input("Unesi duzinu niza: "))
# while n < 3 or n > 100:
#   n = int(input("Duzina niza mora biti od 3 do 100: ")) 

# niz = []
# for i in range(n):
#   el = float(input("Unesi el niza: "))
#   niz.append(el)

# for i in range(1, n-1):
#   if niz[i] == (niz[i-1]+ niz[i+1])/2:
#     print(f"Broj na mestu {i+1} predstavlja ar. sredinu prethodnog i sl. elementa") 

##########################################

# def obimKonveksonog(xKordinate, yKordinate,n):
#   obim = 0
#   for i in range(n):
#     x1, y1 = xKordinate[i], yKordinate[i]
#     x2, y2 = xKordinate[(i+1) % n ], yKordinate[(i+1) % n]

#     udaljenost = math.sqrt((x2-x1)**2 +(y2-y1)**2)
#     obim += udaljenost
#   return obim

# xKordinate = []
# yKordinate = []
# n = int(input("Unesi duzinu kordinata x i y: "))
# while n < 3:
#   n = int(input("Duzina kordinata mora biti najmanje 3: "))
# for i in range(n):
#   x = float(input(f"Unesi {i+1}kordinatu temena x: "))
#   y = float(input(f"Unesi {i+1}kordinatu temena y: "))
#   xKordinate.append(x)
#   yKordinate.append(y)

# rezultat = obimKonveksonog(xKordinate,yKordinate,n)
# print(f"Obim konveksnog ugla je: {rezultat}")

##########################################
# def toDecimal(listaKaraktera):
#   return int(''.join(listaKaraktera), 16)
# listaKaraktera = []
# dozvoljeni_znakovi = "0123456789ABCDEF"
# for i in range(6):
#   while True:
#     karakter = input(f"Unesi {i+1}karakter: ")
#     if karakter not in dozvoljeni_znakovi:
#       print("Karakter mora biti od 1-9 ili A-F. Pokušaj ponovo.")
#     else:
#       listaKaraktera.append(karakter)
#       break

# decimalanBroj = toDecimal(listaKaraktera)
# print(f"Uneti hexBroj: {listaKaraktera} u decimalnom zapisu je: {decimalanBroj}")

##########################################
while True:
  nizX = []
  nizY = []
  n = int(input("Unesi duzinu nizova: "))
  while n < 2:
    n = int(input("Duzina mora biti veca od 2: "))
  for i in range(n):
    Xel = float(input("Unesi elemente nizaX: "))
    Yel = float(input("Unesi elemente nizaY: "))
    nizX.append(Xel)
    nizY.append(Yel)
  
  duzina = 0
  for i in range(1,n):
    dx = nizX[i] - nizX[i-1]
    dy = nizY[i] - nizY[i-1]
    duzina += math.sqrt(dx** + dy**2)
  print(f"Duzina izlomljene linije je: {duzina}")
  ponovo= input("Da li zelis da uneses nove tacke: (da/ne) ")
  if ponovo != "da":
    break