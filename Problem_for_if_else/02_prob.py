age = input("Give me your age ")

age_in_int = int(age)

day = input("Give a day for movie ")

price = 12 if age_in_int >= 18 else 8

if day == "wednesday":
  price -= 2
  print("Movie ticket price is $",price)
else:
  print("Movie ticket price is $",price)