masa = float(input("Unesi telesnu masu(kg): \n"))
visina = float(input("Unesi visinu(metri): \n"))
bmi = masa / (visina**2)
print("Vas bmi je: " + str(bmi))
if bmi < 18.5:
  print("Pothranjena osoba" )
elif 18.5 < bmi < 25:
  print("Osoba normalne telesne mase")
elif 25 < bmi < 30:
  print("Osoba prekomerne telesne mase")
elif bmi > 30:
  print("Gojazna osoba")