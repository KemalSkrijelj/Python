import math as math

# recnik = {"Ime": "Kemal","Godine": 18}
# print(recnik)

# for key in recnik:
#   print(key)
# for value in recnik.values():
#   print(value)
# for key,value in recnik.items():
#   print(key, value)

# del recnik["Ime"]
# print(recnik)

# recnik.clear()
# print(recnik)

##############################

# recnik = {}

# for i in range(5):
# key = input("Unesi key: ")
# value = input("Unesi value: ")
#   recnik[key] = value
# print(recnik)

##############################

# recnik = {}
# n = int(input("Unesi broj el u recniku: "))
# for i in range(n):
#   key = input("Unesi key: ")
#   value = input("Unesi value: ")
#   recnik[key] = value
# print(recnik)

# kljucevi = list(recnik.keys())
# for key in kljucevi:
#   del recnik[key]
#   print(f"Trenutni recnik: {recnik}")

##############################

# recnik = {"Godine": 20, "Godine2": 18, "Godine3": 21, "Godine4": 22, "Godine5": 23}
# parneVrednosti = []
# neparneVrednosti = []
# for value in recnik.values():
#   if value % 2 == 0:
#     parneVrednosti.append(value)
#   else:
#     neparneVrednosti.append(value)
# print(parneVrednosti)
# print(neparneVrednosti)

##############################

def ispisVrednosti(**recnik):
  for key, value in recnik.items():
    print(f"{key}: {value}")

def kljucevi(**recnik):
  for key in recnik:
    print(key, end=" ")

def vrednosti(**recnik):
  for value in recnik:
    print(recnik[value], end= ' ')

recnik = {"Ime": "Kemal", "Prezime": "Skrijelj", "Godine": 18, "Smer": "Softverski inzenjer"}

ispisVrednosti(**recnik)
kljucevi(**recnik)
print("\n")
vrednosti(**recnik)