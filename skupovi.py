import math as math

# torka = (1,2,3)
# skup = set(torka)
# print(torka)
# print(skup)

###########################
# def a(lista1,lista2):
#   s1, s2 = set(lista1), set(lista2)
#   return s1 & s2

# def b(*lista1):
#   sets = [set(l) for l in lista1]
#   return set.intersection(*sets)
# lista1 = [1,2,3]
# lista2 = [3,4,5]

###########################
n = int(input("Unesi duzinu nekog skupa: "))
skup = set()
toRemove = set()

for i in range(n):
  el = int(input("Unesi element: "))
  skup.add(el)

print(skup)

for el in skup:
  if el % 2 == 0:
    print(f"Parni el u skupu: {el}")
    toRemove.add(el)

for el in toRemove:
  skup.remove(el)

print(skup)
