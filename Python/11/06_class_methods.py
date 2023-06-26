class Employee:
    company = "Google"
    name = "Subhash"

    # @classmethod   # This is going to change the class attribute not Instance attributes
    # def changename(self, name):        
    #     self.name = name

    # Method 2
    def changename(self, name):        
        self.__class__.name = name # Here the self__class__ means name of class and here the class is Employee 

class person(Employee): # Here this person class will inherite only the class attributes

    def getInfo(self):
        print(f"Hi, Everyone I am {self.name}") # Here this name only take the class attributes

dippu = Employee()
p = person()
# dippu.name = "Subhash Prasad"
# dippu.name = "Prasad"
print(dippu.name)
# p.getInfo()
dippu.changename("Dippu")
p.getInfo() 
# print(dippu.name)
# print(Employee.name)

























# class Employee:
#     company = "Camel"
#     salary = 100
#     location = "Delhi"

#     # def changeSalary(self, sal):
#     #     self.__class__.salary = sal

#     @classmethod
#     def changeSalary(cls, sal):
#         cls.salary = sal

# e = Employee()
# print(e.salary)
# e.changeSalary(455)
# print(e.salary)
# print(Employee.salary)





































































































































