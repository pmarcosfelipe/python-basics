try:
  number = int(input("Type an integer number: "))
  result = 10 / number
except ValueError as error:
  print(f"Value error: {error}")
  raise ValueError("Variable type incompatible, you should type an integer number!")
except Exception as error:
  print(f"Exception error: {error}")
else:
  print(f"Result: {result}")
finally:
  print("Operation finalized")
