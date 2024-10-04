print("Example of standard module import")
from math import sqrt
from my_module import double, greetings

square = sqrt(25)

print(f"square: {square}")

print("\nCreating and importing a new module")
print(greetings("Marcos"))
print(f"Double of 5 is {double(5)}")