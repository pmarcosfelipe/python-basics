# List declaration

list = [1, 2, 3, 4, 5, "Marcos", True, False]
number_list = [2, 5, 1, 3, 4]

print("list is: ", list)
print("list[3]: ", list[3])
print("list[1:7]: ", list[1:7])
print("list[:5]: ", list[:5])
print("list[2:]: ", list[2:])

# change list elements
list[0] = "CHANGED"
print("changed list is: ", list)


# Methods
list.append(6)
print("list.append(6): ", list)
print("list.index('Marcos'): ", list.index("Marcos"))

list.insert(2, "Vieira")
print("list.insert(): ", list)

removed_element = list.pop(0)
print("list.pop(0): ", removed_element, list)

list.remove(True)
print("list.remove(True): ", list)

number_list.sort()
print("number_list.sort(): ", number_list)

