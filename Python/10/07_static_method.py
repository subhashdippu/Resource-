class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod # This is a kind of a special function which mordifies the function
    def greet():
        print("Good Morning, Sir")

    @staticmethod # This is not takes any participation for class instance
    def time():
        print("The time is 9AM in the morning")

Subhash = Employee()
Subhash.salary = 100000
Subhash.getSalary("Thanks!") # Employee.getSalary(Subhash)
Subhash.greet() # Here this is going to convert into this Employee.greet() 
Subhash.time()

