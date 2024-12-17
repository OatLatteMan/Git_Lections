# oop_human1.py
import sys
sys.setrecursionlimit(10)

# class vs instance/object

class Human:
    def __init__(self, name, age, body_count, best_friend=None):
        self.name = name
        self.age = age
        self.body_count = body_count
        self.best_friend = best_friend

    def introduce(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} years old and my body count is {self.body_count}")

    def rename(self, new_name):
        self.name = new_name

    def get_older(self):
        self.age += 1
        self.introduce()


dima = Human('Dima', 24, 3)
sasha = Human('Sasha', 23, 0, dima)
print(f"Dima's best friend is {dima.best_friend.name}, her age is {dima.best_friend.age} and her body count is {dima.best_friend.body_count}")

dima.introduce()
sasha.introduce()

dima.body_count+=1
dima.get_older()

sasha.body_count+=1
sasha.get_older()

