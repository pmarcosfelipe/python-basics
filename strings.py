name = "Marcos"

lastname = "Vieira"

fullname = "Marcos Vieira"

fullname_triple_quotation_marks = """Marcos
 Vieira"""

fullname_break = "Marcos \
  Vieira"

# Format
print("1 - fullname:", fullname)
print("2 - fullname:" + fullname)
print("3 - fullname:", "Marcos" + "Vieira")
print("4 - fullname:" + "Marcos", "Vieira")
print("5 - fullname:", fullname_triple_quotation_marks)
print("6 - fullname:", fullname_break)
print("7 - fullname: %s" % fullname)
print("8 - fullname: %s %s" % (name, lastname))
print(f"9 - fullname: {name} {lastname}")
print("9 - fullname: {} {}".format(name, lastname))

# String Methods
print("upper():", fullname.upper())
print("lower():", fullname.lower())
print("name[0]:", name[0])
print("fullname.count():", fullname.count("a"))
print("fullname.find():", fullname.find("a"))
print("fullname.encode():", fullname.encode())
print("fullname.encode().decode():", fullname.encode().decode())
print("fullname.replace('a', 'x'):", fullname.replace('a', 'x'))
print("'-'.join(name):", '-'.join(name))
print("fullname.split(" "):", fullname.split(" "))
print("name.strip('M')", name.strip("M"))
print("name.rstrip('M')", name.strip("s"))
print("fullname.startswith('Ma')", fullname.startswith("Ma"))
print("'os' in fullname", "os" in name)
print("'abc' in fullname", "abc" in name)
print("'abc' not in fullname", "abc" not in name)
