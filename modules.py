print("Example of standard module import")
from math import sqrt
from my_module import double, greetings

square = sqrt(25)

print(f"square: {square}")

print("\nCreating and importing a new module")
print(greetings("Marcos"))
print(f"Double of 5 is {double(5)}")


import requests
url = "https://www.example.com"

response = requests.get(url)
print(f"\nHTTP request to {url} returned the status {response.status_code}")