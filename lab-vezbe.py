def unosListe():
  duzina = int(input("Unesi duzinu liste: "))
  print("Unesi elemente liste: ")
  lista = []
  for i in range(duzina):
    element = int(input(" "))
    lista.append(element)
  return lista

def jedanDeljiv(lista, k):
  for element in lista:
    if(element % k == 0):
      return True
  return False

def sviDeljivi(lista, k):
  for element in lista:
    if(element % k != 0):
      return False
  return True

def elementiDeljivi(lista, k):
  deljivi = []
  for element in lista:
        if element % k == 0:
            deljivi.append(element)
  return deljivi

lista = unosListe()
k = int(input("Unesi kolicnik k: "))

if jedanDeljiv(lista,k):
  print(f"Najmanje jedan  je deljiv s {k}")
else:
  print(f"Nije deljiv samo jedan element s {k}")

if sviDeljivi(lista,k):
  print(f"Svi elementi su deljivi s kolicnikom {k}")
else:
  print(f"Nisu svi elementi  deljivi s kolicnikom {k}")

deljivi = elementiDeljivi(lista, k)

if deljivi:
    print(f"Elementi deljivi sa {k} su: {deljivi}")
else:
    print(f"Nema elemenata koji su deljivi s {k}")