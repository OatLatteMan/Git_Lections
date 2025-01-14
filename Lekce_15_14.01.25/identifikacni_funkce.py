# identifikacni_funkce.py

class Car:
    def __init__(self):
        self.name = 'super car'

    def __eq__(self, other):
        return self.name == other.name

class SportCar(Car):
    pass

car = Car()
sport_car = SportCar()

print(car == sport_car)

print(f'Id of car is: {id(car)}')           # idicka se furt obnovuji po spusteni souboru
print(f'Id of sport car is {id(sport_car)}')# protoze nepamatuje predchozi stav

print(f'Type of car is {type(car)}. Type of sport car is {type(sport_car)}')
print(type(car) is Car)

print(isinstance(sport_car, Car))
print(isinstance(sport_car, SportCar))
print(isinstance(sport_car, (SportCar, int)))

print(vars(car))
print(dir(car))

print('getattr, hasattr, setattr, delattr')
setattr(car, 'power', 100)
print(hasattr(car, 'power'))



for name in dir(car):
    if not name.startswith('_'):
        setattr(car, name, None)

print(car.name)
print(car.power)
