import math as math
import struct
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

def kreirajLetove():
  with open("letovi.dat", "w") as f:
    podaci = [
        "1 101 202 150 20 5000.0",
        "2 101 202 100 10 3000.0",
        "3 303 404 200 30 8000.0",
        "4 101 202 120 25 4000.0",
        "5 303 404 180 20 7000.0"
    ]
    f.write("\n".join(podaci))

kreirajLetove()

def prosecnaPotrosnja(ulaznaDatoteka, sifraPoletanja, sifraSletanja):
  ukupnoGorivo = 0.0
  ukupnoPutnika = 0
  with open(ulaznaDatoteka, "r") as ulaz:
    for linija in ulaz:
      linija = linija.strip()
      if linija:
        podaci = linija.split()
        brojLeta = int(podaci[0])
        polaziste = int(podaci[1])   
        odrediste =  int(podaci[2])      
        ekonomska =  int(podaci[3])        
        poslovna = int(podaci[4])      
        gorivo = float(podaci[5])

        if polaziste == sifraPoletanja and odrediste == sifraSletanja:
          ukupnoPutnika += ekonomska + poslovna
          ukupnoGorivo += gorivo
  if ukupnoPutnika == 0:
    print("Nema putnika za poletanje.")

  return ukupnoGorivo / ukupnoPutnika

sifraPoletanja = int(input("Unesi sifru poletanja: "))
sifraSletanja = int(input("Unesi sifru sletanja: "))

rezultat = prosecnaPotrosnja("letovi.dat", sifraPoletanja, sifraSletanja)
print(f"Rezultat: {rezultat} ")