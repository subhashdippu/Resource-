class Employee:
    company = "Google"
    salary = 100

Subhash = Employee()
raj = Employee()

# Creating instance attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400
Subhash.salary = 45
print(Subhash.salary)
print(raj.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 