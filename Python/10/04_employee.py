class Employee:
    company = "Google"
    salary = 100

ram = Employee() # Object instantiation 
raja = Employee()
ram.salary = 300 # Instance attributes are those attributes which are related to object # Shirf ek ke liye
raja.salary = 400

print(ram.company)
print(raja.company)
Employee.company = "YouTube" # Class attributes are those attributes which directly related to class # Creating instance attribute for both the objects
print(ram.company)
print(raja.company)
print(ram.salary)
print(raja.salary)