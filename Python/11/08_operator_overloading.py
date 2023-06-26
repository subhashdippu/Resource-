class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num3): ## Any name is come with double underscore __ like this so this is called dender method
        print("Lets add")
        return self.num + num3.num

    def __mul__(self, num3):
        print("Lets multiply")
        return self.num * num3.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2 # We cann't add the number without the add function because n1 and n2 are not integer no: 
mul = n1 * n2
print(sum)
print(mul)