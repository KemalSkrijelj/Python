import math as math
import struct
import os
# datoteka = open("podaci.txt", "r")
# tekst = datoteka.read(5)
# tekst = datoteka.read(4)
# tekst = datoteka.readline() #cita prvu liniju
# print(tekst)
# for red in datoteka:
#   print("Red teksta je: " + red)
# datoteka.write("Softv. inzenjer\n")

# ime = "Kemal"
# prezime = "Skrijelj"
# brIndexa = 36039
# datoteka.write("{0:40s}{1:40s}{2:10d}".format(ime,prezime,brIndexa))
# ime = datoteka.read(40).strip()
# prezime = datoteka.read(40).strip()
# brojIndexa = int(datoteka.read(10))
# print(f"Ime:  {ime}")
# print(f"Prezime:  {prezime}")
# print(f"Br.Indexa:  {str(brojIndexa)}")
# datoteka.close()

###################################
# def prosekReci(datoteka):
#   with open(datoteka, "r") as dat:
#     tekst = dat.read()
#     reci = tekst.split()
    
#     brojReci = len(reci)
#     brojSlova = sum(len(rec) for rec in reci)
#     srednjaVrednost = brojSlova / brojReci
 
#     return srednjaVrednost

# rezultat =prosekReci("podaci.txt")
# print(rezultat)

###################################

# def ulaznaUbinarnu(ulazna,izlazna):
#   with open(ulazna, encoding="ascii") as ulaz:
#     with open(izlazna, "wb") as izlaz:
#       izlaz.write(ulaz.read().encode("ASCII"))
# def izlaznaUlazna(izlazna,ulazna):
#   with open(izlazna, "rb") as izlaz:
#     with open(ulazna, "w", encoding="ascii") as ulaz:
#       ulaz.write(izlaz.read().decode("ASCII"))

# ulazna = "v05z05d01.txt"
# izlazna = "v05z05d02.bin"

# ulaznaUbinarnu(ulazna, izlazna)
# izlaznaUlazna(izlazna,ulazna)

###################################

# def uIzlanznu(ulazna,izlazna):
#   nadimci = {}
#   with open(ulazna, "r", encoding='utf-8') as ulaz:
#     for linija in ulaz:
#       podaci = linija.strip().split()
#       nadimak = podaci[0]
#       pol = int(podaci[1])
#       ime = podaci[2]

#       if nadimak not in nadimci:
#         nadimci[nadimak] = {"0": [], "1": []}

#       if pol == 0:
#         nadimci[nadimak]["0"].append(ime)
#       elif pol == 1:
#         nadimci[nadimak]["1"].append(ime)
#     with open(izlazna, "w") as izlaz:
#       for nadimak, polovi in nadimci.items():
#         if polovi["0"] and polovi["1"]:
#           izlaz.write(f"{nadimak} 2: {', '.join(polovi['0'] + polovi['1'])}\n")
#         elif polovi['0']:
#           izlaz.write(f"{nadimak} 0: {', '.join(polovi['0'])}\n")
#         elif polovi['1']:
#           izlaz.write(f"{nadimak} 1: {", ".join(polovi['1'])}\n")

# ulazna = "v05z06d01.txt"
# izlazna = "v05z06d02.txt"
# uIzlanznu(ulazna,izlazna)

###################################

# def srednjaDuzina(datoteka):
#   with open(datoteka, "r") as ulaz:
#     tekst = ulaz.read()
#     reci = tekst.split()

#     brojReci = len(reci)
#     brojSlova = 0
#     for rec in reci:
#       brojSlova += len(rec)

#     return brojSlova / brojReci

# rezultat = srednjaDuzina("podaci.txt")
# print(f"Datoteka {rezultat}")

###################################

# def ulazniUIzlazni(ulazni,izlazna):
#   with open(ulazni, "r") as ulaz:
#     with open(izlazna, "wb") as izlaz:
#       izlaz.write(ulaz.read().encode("ASCII"))
# def izlaznaUlazna(izlazni, ulazni):
#   with open(izlazni, "rb") as ulaz:
#     with open(ulazni, "w", encoding="ascii") as izlaz:
#       izlaz.write(ulaz.read().decode("ASCII"))


# ulazni = "v05z05d01.txt"
# izlazna = "v05z05d02.bin"
# ulazniUIzlazni(ulazni, izlazna)
# izlaznaUlazna(izlazna, ulazni)

###################################

# def obrada(ulazna, izlazna):
#   nadimci = {}
#   with open(ulazna, "r") as ulaz:
#     for linija in ulaz:
#       podaci = linija.strip().split()

#       nadimak = podaci[0]
#       pol = int(podaci[1])
#       ime = podaci[2]

#       if nadimak not in nadimci:
#         nadimci[nadimak] = {"0": [], "1": []} 
      
#       if pol == 0:
#         nadimci[nadimak]["0"].append(ime)
#       elif pol == 1:
#         nadimci[nadimak]["1"].append(ime)
#       with open(izlazna, "w") as izlaz: 
#         for nadimak, polovi in nadimci.items():
#           if polovi["0"] and polovi["1"]:
#             izlaz.write(f"{nadimak} 2: {', '.join(polovi["0"] and polovi["1"])}\n")
#           elif polovi["0"]:
#             izlaz.write(f"{nadimak} 0: {', '.join(polovi["0"])}\n")
#           elif polovi["1"]:
#             izlaz.write(f"{nadimak} 1: {', '.join(polovi["1"])}\n")

# ulazna = "v05z06d01.txt"
# izlazna = "v05z06d02.txt"
# obrada(ulazna,izlazna)

###################################
# def ucitajOcene(datoteka):
#   recnikOcena = {}
#   with open(datoteka, "r") as dat:
#     for linija in dat:
#       linija = linija.strip()
#       if linija:
#         podaci = linija.split()
#         ime = podaci[0]
#         ocena = int(podaci[1])
      
#       if ime not in recnikOcena:
#         recnikOcena[ime] = []
#       recnikOcena[ime].append(ocena)
#   return recnikOcena

# def prosekOcena(recnikOcena):
#   for ime, ocene in recnikOcena.items():
#     prosek = sum(ocene) / len(ocene)
#     print(f"{ime} prosek ocena: {prosek}")

# recnikOcena = ucitajOcene("ocene.txt")
# prosekOcena(recnikOcena)

###################################

# def nadjiDuplikate(ulaznaDatoteka, izlaznaDatoteka):
#   brojSifri = {}
#   with open(ulaznaDatoteka, "r") as ulaz:
#     for linija in ulaz:
#       linija = linija.strip()
#       if linija:
#         podaci = linija.split()
#         sifra = int(podaci[0])
#       if sifra not in brojSifri:
#         brojSifri[sifra] = 1
#       else:
#         brojSifri[sifra] += 1
#   with open(izlaznaDatoteka, "w") as izlaz:
#     for sifra, broj in brojSifri.items():
#       if broj >= 2:
#         izlaz.write(f"{sifra}\n")
        
# ulaznaDatoteka = "katalog.txt"
# izlaznaDatoteka = "sifre.txt"
# nadjiDuplikate(ulaznaDatoteka, izlaznaDatoteka)
# print(f"Sifre koje se ponavljaju zapisane su u datoteku {izlaznaDatoteka} ")

###################################

# def kreirajLetove():
#   with open("letovi.dat", "w") as f:
#     podaci = [
#         "1 101 202 150 20 5000.0",
#         "2 101 202 100 10 3000.0",
#         "3 303 404 200 30 8000.0",
#         "4 101 202 120 25 4000.0",
#         "5 303 404 180 20 7000.0"
#     ]
#     f.write("\n".join(podaci))

# kreirajLetove()

# def prosecnaPotrosnja(ulaznaDatoteka, sifraPoletanja, sifraSletanja):
#   ukupnoGorivo = 0.0
#   ukupnoPutnika = 0
#   with open(ulaznaDatoteka, "r") as ulaz:
#     for linija in ulaz:
#       linija = linija.strip()
#       if linija:
#         podaci = linija.split()
#         brojLeta = int(podaci[0])
#         polaziste = int(podaci[1])   
#         odrediste =  int(podaci[2])      
#         ekonomska =  int(podaci[3])        
#         poslovna = int(podaci[4])      
#         gorivo = float(podaci[5])

#         if polaziste == sifraPoletanja and odrediste == sifraSletanja:
#           ukupnoPutnika += ekonomska + poslovna
#           ukupnoGorivo += gorivo
#   if ukupnoPutnika == 0:
#     print("Nema putnika za poletanje.")

#   return ukupnoGorivo / ukupnoPutnika

# sifraPoletanja = int(input("Unesi sifru poletanja: "))
# sifraSletanja = int(input("Unesi sifru sletanja: "))

# rezultat = prosecnaPotrosnja("letovi.dat", sifraPoletanja, sifraSletanja)
# print(f"Rezultat: {rezultat} ")

###################################
# def ucitaniUcenici(datoteka):
#   ucenici = {}
#   with open(datoteka, "r") as d:
#     for linija in d:
#       linija = linija.strip()
#       if linija:
#         podaci = linija.split()
#         ime = podaci[0]
#         ocena = int(podaci[1])

#         if ime not in ucenici:
#           ucenici[ime] = []
#         ucenici[ime].append(ocena)
#   return ucenici

# def prosekOcena(ucenici):
#   for ime, ocena in ucenici.items():
#     prosek = sum(ocena) / len(ocena)
#     print(f"Ucenik: {ime}, prosek ocena: {prosek}")

# datoteka = "ocene.txt"
# ucenik = ucitaniUcenici(datoteka)
# prosekOcena(ucenik)

###################################
# def unesiKatalog(datoteka):
#   n = int(input("Unesi broj filmova koji ces da uneses: "))
#   with open(datoteka, "w") as ulaz:
#     for i in range(n):
#       sifra = input(f"Film[{i+1}], unesi celobrojnu sifru: ")
#       oznaka = input(f"Film[{i+1}], unesi celobrojnu oznaku reginona: ")
#       film = input(f"Film[{i+1}], unesi ime filma: ")
#       ulaz.write(' '.join([sifra, oznaka, film]) + '\n')


# def ponavljanja(ulazna, izlazna):
#   brojSifri = {}
#   with open(ulazna, "r") as ulaz:
#     for linija in ulaz:
#       linija = linija.strip()
#       if linija:
#         podaci = linija.split()
#         sifra = int(podaci[0])
#         region = int(podaci[1])
#         if sifra not in brojSifri:
#           brojSifri[sifra] = 1
#         else:
#           brojSifri[sifra] += 1
#   with open(izlazna, "w") as izlaz:
#     for sifra, broj in brojSifri.items():
#       if broj >= 2:
#         izlaz.write(f"{sifra} \n" )

# ulazna = "katalog.txt"
# izlazna = "sifre.txt"
# ponavljanja(ulazna,izlazna)

###################################

# def prosecnaPotresnja(datoteka, sifraPoletanja, sifraSletanja):
#   brojPutnika = 0
#   ukupnoGoriva = 0.0
#   with open(datoteka, "rb") as ulaz:
#     for linija in ulaz:
#       linija = linija.strip()
#       if linija:
#         podaci = linija.split()
#         polaziste = int(podaci[1])
#         odredsite =  int(podaci[2])
#         ekonomska =int(podaci[3])
#         poslovna = int(podaci[4])
#         gorivo = float(podaci[5])

#         if polaziste == sifraPoletanja and odredsite == sifraSletanja:
#           brojPutnika += ekonomska + poslovna
#           ukupnoGoriva += gorivo
#     if brojPutnika == 0:
#       print("Nema putnika za poletanje")
#   return ukupnoGoriva / brojPutnika


# sifraPoletanja = int(input("Unesi sifru poletanja: "))
# sifraSletanja = int(input("Unesi sifru sletanja: "))
# rezultat = prosecnaPotresnja("letovi.dat", sifraPoletanja, sifraSletanja)
# print(f"Prosecna potrosnja goriva: {rezultat:.2f}")

###################################

def unosPodataka(datoteka):
  n = int(input("Unesi koliko puta se unose studenti: "))
  with open(datoteka, "a") as file:
    for _ in range(n):
      indeks = input("Unesi broj indeksa: ")
      name = input("Unesi ime i prezime: ")
      kolokvijum = input("Unesi kolokvijum(npr. K1): ")
      tacnosti = []
      for j in range(4):
        tacnost = int(input(f"Unesi tacnost {j+1} pitalice(-1,0,1): "))
        tacnosti.append(tacnost)
      brojPoena = input("Unesi broj poena osvojenih na zadatku: ")
      file.write(','.join(map(str, [indeks, name, kolokvijum] + tacnosti + [brojPoena])) + '\n')
      
# unosPodataka("student.csv")
def izracunajPoene(kolokvijum, tacnosti, brojPoena):
  k1,k2,k3 = 30,35,35

  poeniK1 = k1 * tacnosti[0] if tacnosti[0] != -1 else 0
  poeniK2 = k2 * tacnosti[1] if tacnosti[1] != -1 else 0
  poeniK3 = k3 * tacnosti[2] if tacnosti[2] != -1 else 0
  ukupnoPoena = (poeniK1 + poeniK2+ poeniK3) * (int(brojPoena) / 100)

  return poeniK1,poeniK2,poeniK3, ukupnoPoena

def createForStudent(datoteka):
  with open(datoteka, "r") as izlaz:
    for linija in izlaz:
      linija = linija.strip()
      if linija:
        podaci = linija.split(',')
        indeks = podaci[0]
        ime = podaci[1]
        kolokvijum = podaci[2]
        tacnosti = list(map(int, podaci[3:7]))
        brojPoena = podaci[7]

        poeni_k1, poeni_k2, poeni_k3, ukupni_poeni = izracunajPoene(kolokvijum, tacnosti, brojPoena)

        fileName = f"{indeks}_{ime}.txt"
        fileName = fileName.replace('/', '_').replace(' ', '_') 

        if not os.path.exists(fileName):
          with open(fileName, "a") as studentFile:
            studentFile.write(f"K1:{poeni_k1} \n")
            studentFile.write(f"K2:{poeni_k2} \n")
            studentFile.write(f"K3:{poeni_k3} \n")
            studentFile.write(f"Ukupno: {ukupni_poeni} \n")
        else:
          print(f"Datoteka za studenta {ime} ({indeks}) već postoji.")

createForStudent("student.csv")