import random

class User:
    def __init__(self, money = 10):
        self.money = money
        self.stuff = []
        self.name = ''

user1 = User()
user1.name = input('Hey there, what\'s your name? ')
print('Well hi, {name}!'.format(name = user1.name))

class Slots:
    def __init__(self, money = 500):
        self.money = money
        self.stuff = []
        self.symbols1 = ['Lemon', 'Orange', 'Plum', 'Cherry' 'Seven', 'Bell', 'WIN']
        self.symbols2 = ['Lemon', 'Orange', 'Plum', 'Cherry' 'Seven', 'Bell', 'WIN']
        self.symbols3 = ['Lemon', 'Orange', 'Plum', 'Cherry' 'Seven', 'Bell', 'WIN']
    
    def slot_time(self):
        self.money += 1
        output_list = []
        output_list.append(random.choice(self.symbols1))
        output_list.append(random.choice(self.symbols2))
        output_list.append(random.choice(self.symbols3))
        if output_list[0] == output_list[1] and output_list[1] == output_list[2]:
            print('WE HAVE A WINNER!')
        if output_list[0:] == 'Lemon':
            user1.money += 1
            self.money -= 1
            print('Nice. At least you got your money back.')
        else:
            print('better luck next time!')
        return output_list

        

slots1= Slots()

result = slots1.slot_time()

print(result)