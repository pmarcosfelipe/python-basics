person = {
  "name": "John",
  "age": 19,
  "city": "Lisbon"
}

print("person: ", person)
print("person['name']: ", person["name"])

person["lastname"] = "Doe"
print("person['lastname']: ", person["lastname"])

person["age"] = 30
print("person['age']: ", person["age"])

del person["lastname"]
print("del person['lastname']: ", person)


# Methods: keys(), values(), items()
keys = list(person.keys())
print("person.keys(): ", keys)

values = list(person.values())
print("person.values(): ", values)

items = list(person.items())
print("person.items(): ", items)
print("person.items(): ", items[0][1])