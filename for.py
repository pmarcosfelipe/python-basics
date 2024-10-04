list = [1, 2, 3, 4, 5]

for element in list:
  print("list element: ", element)


tuple = (1, 2, 3, 4, 5)

for element in tuple:
  print("tuple element: ", element)


person = {
  "name": "John",
  "age": 30,
  "city": "Lisbon"
}

for key in person.keys():
  print("dictionary key: ", key)

for value in person.values():
  print("dictionary values: ", value)

for key, value in person.items():
  print(f"{key} : {value}")

for number in range(0,10):
  print("number range: ", number)

for index in range(0, len(list)):
  print("index range: ", index)
  print("number range: ", list[index])
  
  if index == 3:
    list[index] = 5
  else:
    list[index] = 0

print("list: ", list)


list_enumerate = ["a", "b", "c"]
for index, value in enumerate(list_enumerate):
  print(f"{key} : {value}")