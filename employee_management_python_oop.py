class Employee:
    def __init__(self, name ,salary):
        self.name=name
        self.salary = salary

class Manager(Employee):
    def __init__(self,name, salary , department ):
        super().__init__(name,salary)
        self.department  = department


#value deya ar calling
mgr = Manager("Alice",7000,"Sales")
print(f" he is {mgr.name} , {mgr.salary}, {mgr.department} ")
