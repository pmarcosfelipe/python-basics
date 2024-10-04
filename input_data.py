age = int(input("How old are you? "))

if age < 18:
  print("juvenile")
elif age == 18:
  print("you are 18 years old")
else:
  print("of legal age")


message = "You can get driving license" if age >= 18 else "You can not get driving license"

print(message)