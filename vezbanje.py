import math as math
# nizA = []
# nizB = []
# nizC = []

# n = int(input("Unesi n: "))
# while n >= 200:
#   n = int(input("N mora biti manje od 200: "))

# print("Unesi elemente za niz A")
# for i in range(n):
#   a = int(input("Unesi element nizaA: "))
#   nizA.append(a)

# print("Unesi elemente za niz B")
# for i in range(n):
#   b = int(input("Unesi element nizaB: "))
#   nizB.append(b)

# print("Niz C:")
# for i in range(n):
#   nizC.append(max(nizA[i],nizB[i]))

# print(f"Niz A: {nizA}")
# print(f"Niz B: {nizB}")
# print(f"Niz C: {nizC}")
#######################################
# niz = []
# n = int(input("Unesi n (3-100): "))

# while n < 3 or n > 100:
#   n = int(input("N mora biti pozitivan i veci od 3 a manji od 100: "))

# for i in range(n):
#   el = float(input("Unesi element: "))
#   niz.append(el)

# for i in range(1, len(niz)-1):
#   if niz[i] == (niz[i-1] + niz[i+1])/2:
#     print(f"Element {niz[i]} s indeksom {i+1} je aritmeticka sredina")

#######################################
def obimPoligona(nizA,nizB, n):
  obim = 0
  for i in range(n):
    obim += math.sqrt((nizA[(i+1) % n] - nizA[i])**2 + (nizB[(i+1) % n] - nizB[i])**2)
  return obim

nizA = []
nizB = []
n = int(input("Unesi n kao broj kordinata temena x i y: "))

for i in range(n):
  element = float(input("Unesi element nizaA: "))
  nizA.append(element)
  
for i in range(n):
  element = float(input("Unesi element nizaB: "))
  nizB.append(element) 

Obim = obimPoligona(nizA, nizB, n)

print(f"Obim: {Obim}")