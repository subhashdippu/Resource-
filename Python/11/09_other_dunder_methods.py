class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num
    
    def __str__(self): ## This dender method is going run when we want to print the object directly
        return f"Decimal Number: {self.num}"
    
    def __len__(self): # We can return any default len of our object
        return 1

n = Number(9)
print(n)
print(len(n)) 