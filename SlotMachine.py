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
        self.symbols1 = ['Lemon', 'Orange', 'Plum', 'Cherry', 'Seven', 'Bell', 'WIN']
        self.symbols2 = ['Lemon', 'Orange', 'Plum', 'Cherry', 'Seven', 'Bell', 'WIN']
        self.symbols3 = ['Lemon', 'Orange', 'Plum', 'Cherry', 'Seven', 'Bell', 'WIN']
    
    def slot_time(self):
        self.money += 1
        user1.money -= 1
        nope_list = ['Oh well.', 'Never mind.', 'How\'s the weather looking?', 'Hm.', '*sings* Luck be a lady toooniiiight...', 'You doing ok?', 'Next time, for sure.']
        output_list = []
        output_list.append(random.choice(self.symbols1))
        output_list.append(random.choice(self.symbols2))
        output_list.append(random.choice(self.symbols3))
        print('You got: {list}'.format(list = output_list))
        if output_list[0] == output_list[1] and output_list[1] == output_list[2]:
            print('WE HAVE A WINNER!')
        if output_list[0:] == 'Lemon':
            user1.money += 1
            self.money -= 1
            print('Nice. At least you got your money back.')
        elif output_list[0:] == 'Orange':
            user1.money += 3
            self.money -= 3
            print('Nice!')
        elif output_list[0:] == 'Plum':
            user1.money += 3
            self.money -= 3
            print('Cool!')
        elif output_list[0:] == 'Cherry':
            user1.money += 5
            self.money -= 5
            print('The sweet taste of victory!')
        elif output_list[0] == 'Cherry' or output_list[1] == 'Cherry' or output_list[2] == 'Cherry':
            user1.money += 1
            self.money -= 1
            print('Nice. Popped a cherry AND got your money back!')
        elif output_list.count('Cherry') == 2: 
            user1.money += 3
            self.money -= 3
            print('Winning it this way is way cooler.')
        elif output_list[0:] == 'Seven':
            user1.money += 10
            self.money -= 10
            print('Lucky for some, and that sum is your bank account.') 
        elif output_list.count('Seven') == 2:
            user1.money += 5
            self.money -= 5
            print('Lady Luck has her eye on you!')
        elif output_list[0:] == 'Bell':
            user1.money += 20
            self.money -= 20
            print('Liberty Egalité! /n That\'s how it goes, right?')
        elif output_list[0:] == 'WIN':
            user1.money += 50
            self.money -= 50
            print('OH WE\'VE GOT THEM BIG BUCKS!')
        else:
            print(random.choice(nope_list))
        return 'Wanna try again?'
        

slots1= Slots()
result = slots1.slot_time()
print(result)
print(int(slots1.money))
print(int(user1.money))