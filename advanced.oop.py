class employee:
    def __init__(self,name ,salary):
        self.name = name
        self.salary = salary
    def get_details(self):
        return (f" Name: {self.name}, Salary: ${self.salary}")
class manager(employee):
    def __init__(self,name ,salary,team_size):
        super().__init__(name,salary)
        self.team_size = team_size

    def get_details(self):
        base_details = super().get_details()


        return f"{base_details}, Team size {self.team_size}"


mgr = manager("Alice", 80000, 5)
print(mgr.get_details())
