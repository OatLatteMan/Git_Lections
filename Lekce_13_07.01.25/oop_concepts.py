
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def say_hello(self):
        print("hello")
    

class Employee(Person):
    def __init__(self, first_name, last_name, number):
        super().__init__(first_name, last_name)
        self.number = number
    
    def tidy_up(self):
        print("I am tiding up")
        self._very_good_cleaning()
    
    def _very_good_cleaning(self):
        print("I am tiding up very well")

class ChiefMaster(Employee):

    def cook(self):
        print("I am cooking")
    
    def _very_good_cleaning(self):
        print("I am tiding up very speedy")

jan = Person("Jan", "Novák")
jana = Employee("Jana", "Nová", 1)
petr = ChiefMaster("Petr", "Levý", 2)

print(jan.first_name)
print(jana.first_name)

petr.cook()
petr.tidy_up()
jana.tidy_up()

# petr._very_good_cleaning() # toto je prvátní metoda neměl bych jí používat mimot třídu