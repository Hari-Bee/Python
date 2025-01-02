import random

class User:
    def __init__(self, money = 10):
        self.money = money
        self.collectables = 0
        self.name = ''

user1 = User()

print(int(user1.money))