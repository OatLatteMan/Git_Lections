# oop_human2.py
import sys
sys.setrecursionlimit(10)

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def __repr__(self):
        # representation in list
        return f"{self.name} {self.age}"

    def add_friend(self, human):
        self.friends.append(human)

dima = Human('Dima', 24)
sasha = Human('Sasha', 23)
anastasiia = Human('Anastasiia', 12)

dima.add_friend(sasha)
dima.add_friend(anastasiia)
sasha.add_friend(dima)
sasha.add_friend(anastasiia)
anastasiia.add_friend(dima)
anastasiia.add_friend(sasha)

print(dima.friends)
print(sasha.friends)
print(anastasiia.friends)

print(dima.friends[0].name)


# print(f"{dima.name} is {dima.age} years old")
# print(f"{sasha.name} is {sasha.age} years old")
