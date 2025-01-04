import math as math

# n = int(input("Unesi duzinu nizova: "))

# a = []
# b = []
# c = []

# for i in range(n):
#   el = int(input("Unesi broj za nizA: "))
#   a.append(el)

# for i in range(n):
#   el = int(input("Unesi broj za nizB: "))
#   b.append(el)

# print(f"Niz a: {a}")
# print(f"Niz b: {b}")

# for i in range(n):
#   c.append(max(a[i],b[i]))

# print(f"Niz c: {c}")

######################################

# n = int(input("Unesi duzinu niza"))
# a = []
# while n < 3 or n > 100:
#   n = int(input("Duzina niza mora biti od 3 do 100: "))

# for i in range(n):
#   el = float(input("Unesi el nizaA: "))
#   a.append(el)

# for i in range(1,n-1):
#   if a[i] == (a[i-1]+a[i+1])/2:
#     print(f"Indeks: {i}") 

######################################

# nizA = []
# nizB = []

# n = int(input("Unesi duzinu za kordinateX i kordinateY: "))
# obim = 0
# for i in range(n):
#   el = float(input("Unesi x-kordinate: "))
#   nizA.append(el)

# for i in range(n):
#   el = float(input("Unesi y-kordinate: "))
#   nizB.append(el)

# for i in range(n):
#   j = (i + 1) % n
#   obim += math.sqrt((nizA[j]-nizA[i])**2 + (nizB[j]- nizB[i])**2)

# print(f"Obim koneksnog poligona je {obim}")

######################################

# niz = []
# n = int(input("Unesi broj karaktera koliko ce imati vas niz: "))

# while n > 6:
#   n = int(input("Niz moze imati max 6 karaktera: "))

# brojevi = "123456789"
# slova = "ABCDEFabcdef"

# for i in range(n):
#   el = input(f"Unesi {i+1} karakter: ").strip()
#   while el not in brojevi + slova:
#     el = input(f"Dozovoljeni karakteri(1-9) i (A...F): ").strip()
#   niz.append(el)

# hexBroj = ''.join(niz)

# decimalanBroj = int(hexBroj, 16)

# print(f"Uneti hex broj {hexBroj} u decimalnom je: {decimalanBroj}")

######################################

# dozvoljeniZnakovi = input("Unesi dozvoljene znakove: ").strip()

# while True:
#   unos = input("Unesi neki string: ").strip()
#   if unos == "":
#     print("Uneli ste prazan string!")
#     break
#   if all(char in dozvoljeniZnakovi for char in unos):
#     if unos == unos[::-1]:
#       print("PALINDROM")
#     else:
#       print("NIJE PALINDROM")
#   else:
#       print("Niz sadrži nedozvoljene znakove!")

######################################

while True:
  n = int(input("Unesi duzinu izlomljenih linija: "))

  while n < 2:
    n = int(input("Duzina mora biti najmanje 2: "))

  nizX = []
  nizY = []
  for i in range(n):
    el = float(input("Unesi elemente nizaX: "))
    nizX.append(el)

  for i in range(n):
    el = float(input("Unesi elemente nizaY: "))
    nizY.append(el)

  duzina = 0
  for i in range(n - 1):
    dx = nizX[i+1] - nizX[i]
    dy = nizY[i+1] - nizY[i]
    duzina += math.sqrt(dx**2 + dy**2)
  print(f"Duzina izlomljenje linije iznosi {duzina}")
  
  ponovo = input("Da li zelite da unesete nove tacke (da,ne)?: ").strip().lower()
  if ponovo != "da":
    break