class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6100

    @property  # This is going to not act like a function # This is also called getter method
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter  # This method is use for set value
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
# e.salary = 300
print(e.totalSalary)  # This is act like a property not like a function thats why we cann't call here like a fuction
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)