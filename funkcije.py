import random

# def pogodiBroj():
#   zamisljenBroj = random.randint(0,100)

#   imeIgraca = input("Unesi svoje ime: \n")
#   print(f"Dobrodosao {imeIgraca}, kompjuter ce zamisliti broj od 0 do 100 moras ga pogoditi. Srecno! ")
#   while True:
#     uneti_broj = int(input("Унеси свој број: "))
#     if uneti_broj > zamisljenBroj:
#       print("Uneti broj je veci od zamisljenog broja.")
#     elif uneti_broj < zamisljenBroj:
#       print("Uneti broj je manji od zamisljenog broja.")
#     else:
#       print(f"Uneti broj {uneti_broj} je zamisljeni broj {zamisljenBroj}.")
#       break

# pogodiBroj()
################################################
# print("Unesi duzinu liste: ")
# duzinaListe = int(input())

# lista = []
# print("Unesi elemente liste: \n")
# suma = 0
# for i in range(duzinaListe):
#   element = int(input(f"Element {i+1}: "))
#   lista.append(element)
#   suma += element

# print(f"Kreirana lista je {lista}")
# prosecnaVrednost = suma / (len(lista))
# print(f"Arihmeticka sredina je {prosecnaVrednost}")
# for element in lista:
#   if(element > prosecnaVrednost):
#     print(f"Element veci od prosecne vrednosti: {element}")
################################################
# def unosListe():
#     duzina = int(input("Unesi duzinu liste: "))
#     print("Unesi elemente liste")
#     lista = []
#     for i in range(duzina):
#       element = int(input(""))
#       lista.append(element)
#     return lista

# def jedanDeljiv(lista, k):
#     for element in lista:
#         if element % k == 0:
#             return True
#     return False

# def sviDeljivi(lista, k):
#     for element in lista:
#         if element % k != 0:
#             return False
#     return True

# lista = unosListe()
# k = int(input("Unesi kolicnik k: "))

# if jedanDeljiv(lista, k):
#     print(f"Bar jedan element liste je deljiv količnikom {k}.")
# else:
#     print(f"Nijedan element liste nije deljiv količnikom {k}.")
# if sviDeljivi(lista, k):
#     print(f"Svi elementi liste su deljivi količnikom {k}.")
# else:
#     print(f"Ne dele se svi elementi liste količnikom {k}.")
################################################
# def unosListe():
#     duzina = int(input("Unesi duzinu liste: "))
#     print("Unesi elemente liste")
#     lista = []
#     for i in range(duzina):
#       element = int(input(""))
#       lista.append(element)
#     return lista

# def rotiraj_listu(lista, k, pravac):
#     if pravac == 'levo':
#         k = k % len(lista)  
#         return lista[k:] + lista[:k]
#     elif pravac == 'desno':
#         k = k % len(lista) 
#         return lista[-k:] + lista[:-k]
#     else:
#         print("Unesi levo ili desno.")
#         return lista
    
# lista = unosListe()
# k = int(input("Unesi broj pozicija za rotaciju: "))
# pravac = input("Unesi pravac rotacije ('levo' ili 'desno'): ").lower()

# rotiranaLista =  rotiraj_listu(lista,k,pravac)
# print(f"Rotirana lista {rotiranaLista}")
################################################
# n = int(input("Unesi duzinu n: "))

# def poVelicini(lista):
#     lista = list(set(lista))
#     lista.sort(reverse=True)  
#     return lista[1]

# def unosListe():
#     print("Unesi elemente liste")
#     lista = []
#     for i in range(n):
#       element = int(input(""))
#       lista.append(element)
#     return lista

# lista = unosListe()
# rezultat = poVelicini(lista)

# print(f"Druga po veličini vrednost je: {rezultat}")
################################################
# def izbacivanjeEL(lista):
#     najveci = max(lista)
#     najmanji = min(lista)

#     while najveci in lista:
#         pozicija = lista.index(najveci) + 1  
#         print(f"Element sa najvećom vrednoscu {najveci} je na poziciji {pozicija}")
#         lista.remove(najveci) 

#     prvi_min = lista.index(najmanji) + 1
#     print(f"Prvi element sa najmanjom vrednoscu {najmanji} je na poziciji {prvi_min}")
#     lista.remove(najmanji)

#     poslednji_min = len(lista) - 1 - lista[::-1].index(najmanji) + 1
#     print(f"Poslednji element sa najmanjom vrednošću {najmanji} je na poziciji {poslednji_min}")
#     lista.remove(najmanji)
    
# n = int(input("Unesi broj elemenata liste: "))
# lista = []
# print("Unesi elemente liste:")
# for i in range(n):
#     lista.append(int(input(f"Element {i+1}: ")))

# izbacivanjeEL(lista)
################################################
# def prosecnaTemp(temperature):
#     return sum(temperature) / len(temperature)

# def najtoplijiDan(temperature):
#     maxTemp = max(temperature)
#     indexDana = temperature.index(maxTemp) + 1
#     return indexDana, maxTemp

# def najhladnijiDan(temperature):
#     minTemp = min(temperature)
#     indexDana = temperature.index(minTemp) + 1  
#     return indexDana, minTemp

# def unosTemp():
#     temperature = []
#     print("Unesite dnevne temperature za sedam dana:")
#     for i in range(7):
#         temp = float(input(f"Temperatura za dan {i + 1}: "))
#         temperature.append(temp)
#     return temperature

# temperatura = unosTemp()
# prosecnaTemperatura = prosecnaTemp(temperatura)
# najtopliji = najtoplijiDan(temperatura)
# najhladniji = najhladnijiDan(temperatura)
# print(f"\nProsečna temperatura za nedelju dana je: {prosecnaTemp}°C")
# print(f"Najtolija  temperatura je {najhladniji}°C")
# print(f"Najhladniji temperatura je {najhladniji}°C")
################################################
# def samoglasnici(reč):
#     samoglasnici = "aeiouAEIOU"
#     for karakter in reč:
#         if karakter not in samoglasnici:
#             return False  
    
#     return True

# def istiPocetak(reči):
#     istoSlovo = []  
    
#     for reč in reči:
#         if reč[0].lower() == reč[-1].lower():  
#             istoSlovo.append(reč)  
    
#     return istoSlovo

# def poDuzini(reči):
#   return sorted(reči, key=len) 

# def unos_reči():
#   n = int(input("Unesite broj reci: "))  
#   reci = []  
      
#   print("Unesite reči:")
#   for _ in range(n):
#       rec = input()
#       reci.append(rec) 
#   return reci

# reči = unos_reči()
# samoglasniciReci = []
# for reč in reči:
#     if samoglasnici(reč):
#         samoglasniciReci.append(reč)
# print(f"Reči koje sadrže samo samoglasnike: {samoglasniciReci}")

# isteReci = istiPocetak(reči)
# print(f"Reči koje počinju i završavaju istim slovom: {isteReci}")

# sortiraneReci = poDuzini(reči)
# print(f"Reči sortirane po dužini: {sortiraneReci}")
################################################
def brojacReci(lista):
    brojanje = {}
    for reč in lista:
        brojanje[reč] = brojanje.get(reč, 0) + 1
    return brojanje

def najduza_reč(lista):
    return max(lista, key=len)

def palindromi(lista):
    return [reč for reč in lista if reč == reč[::-1]]

def unosReci():
    lista = input("Unesite listu reci: ")
    return lista

reci = unosReci()
brojanje = brojacReci(reci)
print("Broj pojavljivanja svake reči:")
for rec, broj in brojanje.items():
    print(f"{rec} se ponavlja {broj} puta")
duzaRec = najduza_reč(reci)
print(f"Najduza rec je {duzaRec}")

