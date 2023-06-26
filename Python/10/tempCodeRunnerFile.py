class Employee:
    salary = 300
    company = "Google"

    def __init__(self):
        print("Genius")
        
    def getInfo(self):
        print(f"I am {self.name}, i am employee of {self.company} and my salary is {self.salary} ")

    @staticmethod
    def greet():
        print("Good Morning Everyone")


Subhash = Employee()
Subhash.name = "Subhash"
# print(Subhash.salary)
Subhash.greet()
Subhash.getInfo()