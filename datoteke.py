import math as math

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

def uIzlanznu(ulazna,izlazna):
  nadimci = {}
  with open(ulazna, "r", encoding='utf-8') as ulaz:
    for linija in ulaz:
      podaci = linija.strip().split()
      nadimak = podaci[0]
      pol = int(podaci[1])
      ime = podaci[2]

      if nadimak not in nadimci:
        nadimci[nadimak] = {"0": [], "1": []}

      if pol == 0:
        nadimci[nadimak]["0"].append(ime)
      elif pol == 1:
        nadimci[nadimak]["1"].append(ime)
    with open(izlazna, "w") as izlaz:
      for nadimak, polovi in nadimci.items():
        if polovi["0"] and polovi["1"]:
          izlaz.write(f"{nadimak} 2: {', '.join(polovi['0'] + polovi['1'])}\n")
        elif polovi['0']:
          izlaz.write(f"{nadimak} 0: {', '.join(polovi['0'])}\n")
        elif polovi['1']:
          izlaz.write(f"{nadimak} 1: {", ".join(polovi['1'])}\n")

ulazna = "v05z06d01.txt"
izlazna = "v05z06d02.txt"
uIzlanznu(ulazna,izlazna)