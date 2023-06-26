# Iterator from a fruits tuple and print values
fruitstup = ("Lemon", "Orange", "Banana")
newit = iter(fruitstup)

# Printing each value from fruitstup
print(next(newit))  # Lemon
print(next(newit))  # Orange
print(next(newit))  # Banana