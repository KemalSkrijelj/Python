# brojGodina = int(input("Unesi broj godina radnog staza: \n"))

# if ( brojGodina > 5 ):
#   print(" Ispunjavaš uslovza napredovanje.")
# else: 
#   print(" Potrebno je još iskustva.")
# ##########################################
# emailAdresa = str(input("Unesi email: \n"))

# if ("@" in emailAdresa):
#   print("Email sadrzi @")
# else: 
#   print("Email ne sadrzi @")
# ############################# 
# lozinka = str(input("Unesi jaku lozinku, mora sadrzati brojeve i slova: \n"))
# duzinaLozinke = len(lozinka)
# if (duzinaLozinke > 8):
#   print("Lozinka je jaka")
# else: 
#   print("Lozinka je prekratka")
# #############################
# days = str(input("Unesi neki dan u nedelji \n"))

# if days == "Subota" or days == "Nedelja":
#   print("Vikend")
# else:
#   print("Radni dan")
###############################
# nekiBr = int(input("Unesi trocifren broj: \n"))

# prvaCifra = nekiBr // 100
# drugaCifra = (nekiBr // 10) % 10
# zadnjaCifra = nekiBr % 10

# if (prvaCifra ** 3 + drugaCifra ** 3 + zadnjaCifra ** 3) == nekiBr:
#   print("Ovo je Armstrongov broj")
# else:
#   print("Ovo nije Armstrongov broj")
################################
x = int(input("Unesi x: \n"))
n = int(input("Unesi n: \n"))

for a in range(x,n):
  for b in range(x,n):
    print(a,b)
