import math
import re

import re._compiler
# brojGodina = int(input("Unesi broj godina radnog staza: \n"))

# if ( brojGodina > 5 ):
#   print(" Ispunjavaš uslovza napredovanje.")
# else: 
#   print(" Potrebno je još iskustva.")
# ##########################################
# emailAdresa = str(input("Unesi email: \n"))

# if ("@" in emailAdresa):
#   print("Email sadrzi @")
# else: 
#   print("Email ne sadrzi @")
# ############################# 
# lozinka = str(input("Unesi jaku lozinku, mora sadrzati brojeve i slova: \n"))
# duzinaLozinke = len(lozinka)
# if (duzinaLozinke > 8):
#   print("Lozinka je jaka")
# else: 
#   print("Lozinka je prekratka")
# #############################
# days = str(input("Unesi neki dan u nedelji \n"))

# if days == "Subota" or days == "Nedelja":
#   print("Vikend")
# else:
#   print("Radni dan")
###############################
# nekiBr = int(input("Unesi trocifren broj: \n"))

# prvaCifra = nekiBr // 100
# drugaCifra = (nekiBr // 10) % 10
# zadnjaCifra = nekiBr % 10

# if (prvaCifra ** 3 + drugaCifra ** 3 + zadnjaCifra ** 3) == nekiBr:
#   print("Ovo je Armstrongov broj")
# else:
#   print("Ovo nije Armstrongov broj")
################################
# x = int(input("Unesi x: \n"))
# n = int(input("Unesi n: \n"))

# for a in range(x,n):
#   for b in range(x,n):
#     print(a,b)
############# 7
# rec = input("Unesi neku rec: \n")
# duzina = len(rec)
# if duzina > 5:
#   print("Duga rec")
# else:
#   print("kratka rec")
############# 9
# broj = int(input("Unesi pozitivan ceo br: \n"))

# while broj >= 10:
#   zbir = 0

#   while broj > 0:
#     cifra = broj % 10
#     zbir = zbir + cifra
#     broj = broj // 10
#   broj = zbir
# print(f"Digitalni koren broja je: {broj}")
############### 10
# prviBroj = int(input("Unesi prvi broj: \n"))
# drugiBroj = int(input("Unesi drugi broj: \n"))
# treciBroj = int(input("Unesi treci broj: \n"))

# proizvodBrojeva = prviBroj * drugiBroj * treciBroj

# if proizvodBrojeva % 2 == 0:
#   print("Proizvod je paran")
# else:
#   print("Proizvod je neparan.")
################ 11
# nekiBr = int(input("Unesi neki broj: \n "))
# apsolutnaVrednost = abs(nekiBr)

# if apsolutnaVrednost < 10:
#   print("Apsolutna vrednost je manja od 10")
# else:
#   print("Apsolutna vrednost je veća ili jednaka 10.")
################ 12
# a = float(input("Unesi prvi broj: \n"))
# b = float(input("Unesi drugi broj: \n"))

# zlatniRez = (1 + math.sqrt(5)) / 2

# odnos = a/b if a > b else b / a

# zaokruzivanje = 0.01

# if  abs(odnos - zlatniRez) < zaokruzivanje:
#   print("Brojevi su u zlatnom rezu")
# else:
#   print("Brojevi nisu u zlatnom rezu")
################ 13
# prviBroj = int(input("Unesi prvi broj: \n"))
# drugiBroj = int(input("Unesi drugi broj: \n"))

# n = 1
# while drugiBroj**n < prviBroj:
#     n = n + 1 

# if prviBroj == drugiBroj**prviBroj:
#   print("Prvi broj je stepen drugog broja")
# else:
#   print("Drugi broj je stepen prvog broja")
################ 14
# unetiBr = int(input("Unesi broj: \n"))
# stepenUnetogBr = unetiBr**2

# if stepenUnetogBr % 2 == 0:
#   print("Kvadrat unetog broja je paran.")
# else: 
#   print("Kvadrat unetog broja je neparan.")
################# 15
# prvaStranica = float(input("Unesi prvu stranicu trougla: \n"))
# drugaStranica = float(input("Unesi drugu stranicu trougla: \n"))
# trecaStranica = float(input("Unesi trecu stranicu trougla: \n"))

# if (prvaStranica + drugaStranica > trecaStranica) and (prvaStranica + trecaStranica > drugaStranica) and (drugaStranica + trecaStranica > prvaStranica):
#   print("Ove stranice mogu formirati trougao")
# else:
#   print("Ove stranice ne mogu formirati trougao")

################## 16
# prviBroj = int(input("Unesi prvi broj: \n"))
# drugiBroj = int(input("Unesi drugi broj: \n"))
# treciBroj = int(input("Unesi treci broj: \n"))


# if drugiBroj - prviBroj == treciBroj - drugiBroj :
#   print("Aritmetički niz")
# else:
#   print("Nije aritmetički niz")
################## 18
# prviUgao  = int(input("Unesi prvi ugao: \n"))
# drugiUgao = int(input("Unesi drugi ugao: \n"))
# treciUgao = int(input("Unesi treci ugao: \n"))
# cetvrtiUgao = int(input("Unesi cetvrti ugao: \n"))

# zbirUglova = prviUgao + drugiUgao + treciUgao + cetvrtiUgao

# if zbirUglova == 360 and prviUgao == 90 and drugiUgao == 90 and treciUgao == 90 and cetvrtiUgao == 90:
#   print("Validan pravougaonik")
# else:
#   print("Nije validan pravougaonik.")
################## 19 
# godina = int(input("Unesi godinu: \n"))

# godina_str = str(godina) #Pretvaramo u string

# duzinaGodine = len(godina_str) # Pa racunamo koliko ima cifara

# if duzinaGodine > 4 and duzinaGodine < 4:
#   print("Unesi ovogodisnju godinu")
# else:
#   print(f"Uneli ste {godina} godinu")

# if godina >= 2020 and godina <= 2029:
#   print("Unutar dekade")
# else:
#   print("Van dekade")
################# 20
# unetiBr = int(input("Unesi petocifreni broj: \n"))
# toString = str(unetiBr)
# obrnuti = ''.join(reversed(toString)) ## Pretvaramo u string ponovo jer reversed se koristi za object


# if toString == obrnuti:
#   print("Broj je palindrom")
# else:
#   print("Broj nije palindrom")
################## 21
# broj = int(input("Unesi  broj: \n"))
# zbir = 0
# while broj > 0:
#   cifra = broj % 10
#   zbir +=cifra
#   broj //= 10
# if broj % zbir == 0:
#   print("Broj je deljiv s zbirom svojih cifara")
# else:
#   print("Broj nije deljiv s zbirom svojih cifara") 
################## 22
# rec = input("Unesi neku rec: \n")

# if "a"and"e"and"i"and"o"and"o" in rec:
#   print("Reč sadrži sve samoglasnike")
# else:
#   print("Reč ne sadrži sve samoglasnike.")
################# 23
# dani_u_mesecima = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# mesec = int(input("Unesi broj nekog meseca: \n"))
# dan = int(input("Unesi dan u unetom mesecu: \n"))

# if mesec >= 1 and mesec <= 12:
#   if 1 <= dan <= dani_u_mesecima[mesec - 1]:
#     print("validan datum")
#   else:
#     print("Nevalidan datum")
# else:
#   print("Nevalidan mesec")  
################# 24
# ime = input("Unesi ime: \n")
# duzina = len(ime)

# if duzina > 15:
#   print("Predugacko ime")

# if ime[-1] == "a":
#   print("Zensko ime")
# else:
#   print("Musko ime")
# ################## 25
# a = float(input("Unesi prvi broj: \n"))
# b = float(input("Unesi drugi broj: \n"))
# c = float(input("Unesi treci broj: \n"))

# d = b**2 - 4  *a*c

# if d >= 0:
#   print("Realna resenja")
# else:
#   print("Kompleksna resenja")
################## 26
# broj = int(input("Unesi trocifreni broj: \n"))

# if 100 > broj > 999:
#   print("broj nije trocifren")

# prvaCifra = broj // 100
# drugaCifra = (broj // 10) % 10
# trecaCifra = broj % 10

# izraz = (prvaCifra* (drugaCifra**2)) - trecaCifra**2
# if broj == izraz:
#   print("Zadovoljava")
# else:
#   print("Ne zadovoljava")
################# 27
# masa = float(input("Unesi telesnu masu(kg): \n"))
# visina = int(input("Unesi visinu(metri): \n"))
# bmi = masa / (visina**2)
# print(bmi)
# if bmi < 18.5:
#   print("Pothranjena osoba" )
# elif 18.5 < bmi < 25:
#   print("Osoba normalne telesne mase")
# elif 25 < bmi < 30:
#   print("Osoba prekomerne telesne mase")
# elif bmi > 30:
#   print("Gojazna osoba")
################# 28
# unetiBr = int(input("Unesi broj: \n"))
# unesiOperaciju = input("Deljenje ili Mnozenje? \n").lower()
# if unesiOperaciju == "deljenje":
#   rezultat = unetiBr >> 3
#   print("Deljenje=" + str(rezultat))
# if unesiOperaciju == "mnozenje".lower():
#   rezultat = unetiBr << 1
#   print("Mnozenje=" + str(rezultat))
################# 29
# unetiBr = int(input("Unesi broj: \n"))
# a = 0
# b = 1

# for _ in range(unetiBr):
#   pomocna = a + b
#   a = b
#   b = pomocna
#   print(f"Prvih {unetiBr} članova Fibonacijevog niza: {a, b, a+ b}")
# ################## 30
# unetiBr = int(input("Unesi neki broj: \n"))
# a,b= 0,1
# pomocna = 0
# while b < unetiBr:
#   pomocna = a
#   a = b
#   b = a + pomocna #1 

# if b == unetiBr:
#   print("Broj je u fibonacijevom nizu")
# else:
#   print("Broj nije u fibonacijevom nizu")
# ################## 31
# nekiBroj = int(input("Unesi neki broj: \n"))
# zbirDelilaca = 0

# for i in range(1, nekiBroj):
#   if nekiBroj % i == 0:
#     zbirDelilaca = zbirDelilaca+i

# if zbirDelilaca == nekiBroj:
#   print("Broj je savrsen")
# else:
#   print("Broj nije savrsen")
#############################
# brojevi = [1,2,3,4,4,5,6,6,7]
# sumaCifara = 0

# for i in brojevi:
#   sumaCifara = sumaCifara + i

# print("Suma cifara je:" , sumaCifara)

# rec = "Programiranje"
# brojac = 0

# for slova in rec:
#   if slova == "r":
#     brojac = brojac+1

# print("Broj slova r je :" , brojac)
############################# 32
# broj = int(input("Unesi neki broj: \n"))
# prost = True
# for i in range(2, broj // 2 + 1 ):
#   if broj % i == 0:
#     prost = False
#     break

# if prost:
#   print("Broj je prost")
# else:
#   print("Broj nije prost")
############################# 35
# broj1 = int(input("Unesi prvi broj: \n"))
# broj2 = int(input("Unesi drugi broj: \n"))
# broj3 = int(input("Unesi treci broj: \n"))

# srednjaVrednost = (broj1 + broj2 + broj3) / 3
# brojevi = [broj1, broj2, broj3]
# brojevi.sort()
# medijana = brojevi[1]

# if srednjaVrednost == medijana:
#   print("Srednja vrednost je jednaka medijani")
# else:
#   print("Srednja vrednost nije jednaka medijani")
####################################
# n = int(input("Unesi neki broj: \n"))

# while n >= 10:
#   sumNumbers = 0
#   while n > 0:
#     zadnjaCifra = n % 10
#     sumNumbers += zadnjaCifra
#     n = n // 10
#   n = sumNumbers

# print(f"Digitalni koren je {n} ")
#################################
# prvi = int(input("Prvi broj: \n"))
# drugi = int(input("Drugi broj: \n"))

# zlatniRez = 1.618

# manji = min(prvi ,drugi)
# veci = max(prvi ,drugi)

# odnos = veci / manji
# tolerancija = 0.01

# if abs(odnos - zlatniRez) < tolerancija:
#   print("U zlatnom rezu")
# else:
#   print("Nisu u zlatnom rezu")
#################################
# prvi = int(input("Prvi broj: \n"))
# drugi = int(input("Drugi broj: \n"))

# c = 1
# while drugi**c <= prvi :
#   if drugi ** c == prvi:
#     print("Prvi broj je stepen drugog broja")
#     break
#   c = c+1
# else:
#    print("Prvi broj nije stepen drugog broja")
#################################
# broj = int(input("Unesi broj: \n"))
# zbir = 0
# for i in range(1, broj):
#   if broj % i == 0:
#     zbir += i
# if zbir == broj:
#   print("Savrsen broj")
# else:
#   print("Broj nije savrsen")
############################
# broj = int(input("Unesi broj: \n"))
# uStr = str(broj)
# print("Uneli ste broj: \n" + uStr)
# obrnutiBroj = ''.join(reversed(uStr))
# print("Obrnuti broj je: " + obrnutiBroj)
############################
# n = int(input("Unesite ceo broj n za izračunavanje faktorijela: "))
# fakt = 1
# for i in range(1, n+1):
#   fakt *= i

# print(f"Faktorijel broj {n} je {fakt}") 
############################
# a = input('Prva vrednost = ')
# b = input('Druga vrednost = ')
# print('pre razmene a =', a, 'b =', b)
# pomocna = a
# a = b
# b = pomocna
# print('posle razmene a =', a, 'b =', b)
############################
# broj = int(input("Unesi broj: \n"))
# prost = True
# for i in range(1, broj + 1):
#   if broj % i == 0:
#     prost = False
#     break
# if prost:
#   print("Broj je prost")
# else:
#   print("Broj nije prost")
############################
# n = int(input('Prva vrednost = '))
# a = 0
# b = 1
# pomocna = 0
# while b < n:
#   pomocna = a
#   a = b
#   b = a + pomocna
# if b == n:
#   print("Broj je u fibonacijevom nizu")
# else:
#   print("Broj nije u fibonacijevom nizu")
# ##############################
# a = int(input("Unesi prvu vrednost: \n"))
# b = int(input("Unesi drugu vrednost: \n"))
# c = int(input("Unesi trecu vrednost: \n"))
# d = b**2 - 4*a*c

# if d >= 0:
#   print("Realna resenja")
# else:
#   print("Kompleksna resenja")
# ##############################
# while True:
#   ime = str(input("Unesi ime: \n"))
#   duzina = len(ime)

#   if duzina > 15:
#     print("Predugacko ime")
#     break
#   else:
#     print(f"Vase ime je {ime}")
  
#   if ime[-1] == "a":
#     print("Zensko ime")
#     break
#   else:
#     print("Musko ime")
#     break
# ##############################
# daniUMesecu = [31,28,31,30,31,30,31,30,31,30,31,30]
# mesec = int(input("Unesi mesec kao broj: \n"))
# dan = int(input("Unesi dan u mesecu: "))
# if 1 <= mesec <= 12:
#   if dan <= daniUMesecu[mesec - 1]:
#     print("Validan datum")
#   else:
#     print("Datum nije validan")
# ##############################
# cifra = int(input("Unesi petocifreni broj: \n"))
# toStr = str(cifra)
# obrnutiBroj = ''.join(reversed(toStr))

# if obrnutiBroj == toStr:
#   print("Broj je palindrom")
# else:
#   print("Broj nije palindrom")
################################
# nekiBr = int(input("Unesi br: \n"))
# kvadratBroja = nekiBr**2

# if kvadratBroja % 2 == 0:
#   print("Kvadrat unetog broja je paran")
# else:
#   print("Kvadrat unetog broja nije paran")
################################
# n = int(input("Unesi neki broj: \n"))
# orginalanBroj = n
# zbirCifara = 0
# while n > 0:
#   cifra = n % 10
#   zbirCifara += cifra
#   n = n // 10

# if orginalanBroj % zbirCifara == 0: 
#   print("Broj je deljiv zbirom svojih cifara")
# else:
#   print("Broj nije deljiv zbirom cifara")
################################
# a = int(input("Unesi prvu vrednost: \n"))
# b = int(input("Unesi drugu vrednost: \n"))
# c = int(input("Unesi trecu vrednost: \n"))
# srednjaVrednost = (a+b+c)/3
# brojevi = [a,b,c]
# brojevi.sort()
# medijana = brojevi[1]

# if srednjaVrednost == medijana:
#   print("Srednja vrednost je jednaka medijani")
# else:
#   print("Srednja vrednost je jednaka medijani")
################################
# n = int(input("Unesi neki broj: \n"))
# zbir_delilaca = 0

# for i in range(1, n):
#   if n % i == 0:
#     zbir_delilaca +=i

# if zbir_delilaca == n:
#   print("Savrsen broj")
# else:
#   print("Broj nije savrsen")
################################
# n = int(input("Unesi neki broj: \n"))
# prost = True

# for i in range(2, n):
#   if n % i == 0:
#     prost = False
#     break

# if prost:
#   print("Broj je prost")
# else:
#   print("Broj nije prost")
################################
# n = int(input("Unesi neki broj: \n"))
# a, b = 0,1
# pomocna = 0
# while b < n:
#   pomocna = a
#   a = b
#   b = pomocna + a
# if b == n:
#   print("Broj je deo fib. niza")
# else:
#   print("Broj nije deo fib. niza")
################################
# n = int(input("Unesi neki broj n: \n"))
# a = 0
# b = 1

# for _ in range(n):
#   pomocna = a + b
#   a = b
#   b = pomocna
#   print(f"Prvi {n} clanovi Fib. niza su: {a,b , a+b}")
# ################################
# broj = int(input("Unesi broj: \n"))
# operacija = str(input("Unesi sta zelis mnozenje ili deljenje: \n"))

# if operacija == "mnozenje":
#   rezultat = broj << 1
#   print(rezultat)
# else:
#   rezultat = broj >> 3
#   print(rezultat)
# ################################
# godina = int(input("Unesi godinu unutar dekade(2020-2029): \n"))

# if 2020 <= godina <= 2029:
#   print("Unutar dekade.")
# else:
#   print("Izvan dekade")
# ################################
# prviUgao = int(input("Unesi prvi ugao: \n"))
# drugiUgao = int(input("Unesi drugi ugao: \n"))
# treciUgao = int(input("Unesi treci ugao: \n"))
# cetvrtiUgao = int(input("Unesi cetvrti ugao: \n"))

# zbirUglova = prviUgao + drugiUgao + treciUgao + cetvrtiUgao

# if zbirUglova == 360 and prviUgao == 90 and drugiUgao == 90 and treciUgao == 90 and cetvrtiUgao == 90:
#   print("Validan pravougaonik")
# else:
#   print("Nije validan pravougaonik")
# ################################
# prviBroj = int(input("Unesi prvi broj: \n"))
# drugiBroj = int(input("Unesi drugi broj: \n"))
# stepen = 1

# while drugiBroj**stepen < prviBroj:
#   stepen += 1

# if prviBroj == drugiBroj**prviBroj:
#   print("Prvi broj je stepen drugog broja")
# else:
#   print("Prvi broj nije stepen drugog broja")
# ################################
# prviBroj = int(input("Unesi prvi broj: \n"))
# drugiBroj = int(input("Unesi drugi broj: \n"))
# zlatniRez = 1.618
# manji = min(prviBroj ,drugiBroj)
# veci = max(prviBroj ,drugiBroj)

# odnos = veci / manji
# tolerancija = 0.01
# if abs(odnos - zlatniRez) < tolerancija:
#   print("Brojevi su u zlatnom rezu")
# else:
#   print("Brojevi nisu u zlatnom rezu")
# ################################
# broj = int(input("Unesi trocifren broj: \n"))
# prvaCifra = broj // 100
# drugaCifra = ( broj // 10) % 10
# trecaCifra = broj % 10

# if prvaCifra**3 + drugaCifra**3 + trecaCifra**3 == broj:
#   print("Armnstrongov broj")
# else:
#   print("Nije Arm. broj")
# ################################
# x = int(input("Unesi x: \n"))
# n = int(input("Unesi n: \n"))

# for a in range(x,n):
#   for j in range(x,n):
#     print(a,j)
# ################################
# n = int(input("Unesi pozitivan ceo broj: \n"))
# while n >= 10:
#   zbir = 0
#   while 0 < n:
#     zadnjaCifra = n % 10
#     zbir += zadnjaCifra
#     n = n // 10
#   n = zbir
# print(f"Digitalni koren broja je {n} ")
# ################################
# dani_u_mesecima = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# mesec = int(input("Unesi mesec: (brojevima) \n"))
# dan = int(input("Unesi dan: (brojevima) \n"))

# if 1<= mesec <= 12:
#   if dan >= 1 and dan <= dani_u_mesecima[mesec-1]:
#     print("Validan datum")
#   else:
#     print("Nevalidan datum")
# else:
#   print("Mesec mora biti u opsegu od 1 do 12!")
# ################################
# nekiBroj = int(input("Unesi petocifreni broj: \n"))
# toStr = str(nekiBroj)
# obrnuti = ''.join(reversed(toStr))

# if toStr == obrnuti:
#   print("Broj je palindrom")
# else:
#   print("Broj nije palindrom")
# ################################
# prviBroj = int(input("Unesi prvi broj: \n"))
# drugiBroj = int(input("Unesi drugi broj: \n"))
# treciBroj = int(input("Unesi treci broj: \n"))

# if  drugiBroj - prviBroj == treciBroj - drugiBroj:
#   print("Aritmeticki niz")
# else:
#   print("Nije aritmeticki niz")
# ################################
# broj = int(input("Unesi pozitivan ceo broj: \n"))

# if broj >= 10:
#   zbir = 0
#   while broj > 0:
#     cifra = broj % 10
#     zbir += cifra
#     broj = broj // 10
#   broj = zbir
# print(f"Digitalni broj je {broj}")
# ################################
# broj = int(input("Unesi pozitivan ceo broj: \n"))
# zbir_delilaca = 0

# for i in range(1,broj):
#   if broj % i == 0:
#     zbir_delilaca +=i

# if zbir_delilaca == broj:
#   print("Broj je savrsen")
# else:
#   print("Broj nije savrsen")
# ################################
# broj = int(input("Unesi broj: \n"))
# a,b = 0,1
# pomocna = 0
# while b < broj:
#   pomocna = a
#   a = b
#   b = a + pomocna

# if b == broj:
#   print("Broj je deo fib. niza")
# else:
#   print("Broj nije deo fib. niza")
# ################################
# n = int(input("Unesi broj: \n"))
# a,b = 0,1

# for _ in range(n):
#   pomocna = a + b
#   a = b
#   b = pomocna
#   print(f"Prvih {n} clova Fib. niza su : {a,b, a+b} ")
# ################################
# matrica = [[1,2,3], [2,3,4], [1,2,4]]

# for red in matrica:
#   for element in red:
#       print(element)

# torka = (1,2,"tekst", 3, False)
# print(*torka)
# ################################
# n = int(input("Unesi n: "))
# m = int(input("Unesi m: "))
# matrica = []
# for i in range(n):
#   red = []
#   for j in range(m):
#     red.append((float(input(f"Element matrice ({i+1}, {j+1}): "))))
#   matrica.append(red)

# for red in matrica:
#    print(red)
# ################################
# def f1(l1,l2):
#   s1,s2=set(l1),set(l2)
#   return s1.intersection(s2)

# def f2(**liste):
#   sets=[set(l) for l in liste]
#   return sets.intersection(*sets)

# def f3(*liste):
#   sets=[set(l) for l in liste]
#   razlika =[]
#   for i in (len(sets)):
#     set[0], set[i] = set[i], set[i]
#     razlika.append(set.difference(*sets))
#   return set.union(*razlika)

# l1,l2,l3 = [8,5,3,6],[8,9,0,7,3],[0,3,5,6,2]
# s1,s2,s3 = f1(l1,l2), f2(l1,l2,l3), f3(l1,l2,l3)

# print("a:{}\n b:{}\n c:{}".format(f1,f2,f3))
# ################################
# def haterogram(recenica):
#   slova = [slovo for slovo in recenica if slovo.isalpha()]
#   return len(set(recenica)) == len(slova)

# recenicaUneta = input("Unesi recenicu: \n")

# if(haterogram(recenicaUneta)):
#   print(f"{recenicaUneta} je heterogram")
# else:
#   print(f"{recenicaUneta} nije heterogram")
# ################################
# lista = [1,3,"text", 7]

# recnik = {
#   "kljuc1": 1,
#   "element": 3,
#   "txt": "text",
#   "kljuc1": 7
# }

# print(recnik)
# print(recnik.keys())
# print(recnik.values())
# print(recnik.items())

# for i in recnik:
#   print(i, recnik[i])
# ################################
# tekst = r"Studenti \n softverskog \t inzenjerstva"
# print(tekst)
# ################################

# tekst1=re.compile(r"rec")
# tekst2=re.compile(r"od")

# string = "Reci u recenici"

# print(tekst1.search(string))

# for trazeni in tekst1.finditer(string):
#   print(trazeni)
# ################################
# def pronadji_godine(filename):
#   with open(filename) as file:
#     teskt=file.read()
#   pattern = re.compile(r"\d\d\d\d")
#   godine=pattern.findall(teskt)
#   godine.sort(reverse=True)
#   return godine

# datoteka = input("Unesi ime datoteke: \n")
# godine=pronadji_godine(datoteka)
# print("Godine izbora saradnika u nastavi:",",".join(godine))
# ################################

def urediSadrzaj(filename):
  with open(filename, "r+",encoding="UTF-8") as file:
    tekst=file.read()
    pattern = re.compile(r"(\d{1,4})/\d{2}(\d{2}),\s+(\w+)\s+(\w+)")
    noviTekst =pattern.sub(r"\2/\1,\4 \3",tekst)
    file.seek(0)
    file.truncate()
    file.write(noviTekst)

datoteka = input("Unesi naziv datotekeL: ")
urediSadrzaj(datoteka)