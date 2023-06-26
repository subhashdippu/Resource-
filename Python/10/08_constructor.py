class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name # Here the self means object and self.name will set the name as object attribute of self object
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!") 

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

Subhash = Employee("Subhash", 100, "YouTube")
# Subhash = Employee() --> This throws an error (missing 3 required positional arguments:)
Subhash.getDetails()