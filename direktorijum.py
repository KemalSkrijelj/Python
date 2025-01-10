import os

lokacija = os.getcwd()
rezultat = os.listdir(lokacija)
fajl = open("novaDat.txt", "w")

for x in rezultat:
  fajl.write(x + '\n')

fajl.close()