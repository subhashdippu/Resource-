class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}") # Here self means Subhash * Object attribute 

Subhash = Employee()
Subhash.salary = 100000
Subhash.getSalary() # This is going to convert into this Employee.getSalary(Subhash) * Here Subhash is the prameter for self # Fuctions are belongs to Object