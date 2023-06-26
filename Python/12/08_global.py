a = 54 # Global variable
print(f"Print statement 3: {a}")
def func1():
    global a
    a = 6
    print(f"Print statement 1: {a}")
    # a = 8 # Local Variable if global keyword is not used
    print(f"Print statement 2: {a}")

func1()
print(f"Print statement 3: {a}")