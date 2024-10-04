def greeting(name):
  print(f"Hello, {name}!")

print("\ncalling function greeting()... ")
greeting("Marcos")


def calculateNumberSquare(number):
  result = number ** 2
  return result

print("\ncalling function calculateNumberSquare()... ", calculateNumberSquare(2))

def sumNumbers(number1, number2):
  result = number1 + number2
  return result

print("\ncalling function sumNumbers()... ", sumNumbers(2, 4))
