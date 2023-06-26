def greet(name):
    print(f"Good morning, {name}")

# print(__name__) # This will run for another files mean import Here it will print the name of this file
if __name__ == "__main__": # Here it will change the file name with the name main, because of this the code written bellow only run with this program
    n = input("Enter a name ") # Here we check first name == main then the code will run
    greet(n)
