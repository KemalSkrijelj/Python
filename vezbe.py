import math
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
prvi = int(input("Prvi broj: \n"))
drugi = int(input("Drugi broj: \n"))

c = 1
while drugi**c <= prvi :
  if drugi ** c == prvi:
    print("Prvi broj je stepen drugog broja")
    break
  c = c+1
else:
   print("Prvi broj nije stepen drugog broja")