import random

class User:
    def __init__(self, money = 10):
        self.money = money
        self.stuff = []
        self.name = ''

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
        print(' ')
        print('You got: {}'.format(output_list))
        if output_list[0:] == 'Lemon':
            user1.money += 1
            self.money -= 1
            print('+1 credit. Nice. At least you got your money back.')
        elif output_list[0:] == 'Orange':
            user1.money += 3
            self.money -= 3
            print('+3 credits. Nice!')
        elif output_list[0:] == 'Plum':
            user1.money += 3
            self.money -= 3
            print('+3 credits. Cool!')
        elif output_list[0:] == 'Cherry':
            user1.money += 5
            self.money -= 5
            print('+5 credits. The sweet taste of victory!')
        elif output_list.count('Cherry') == 2: 
            user1.money += 3
            self.money -= 3
            print('+3 credits. Winning it this way is way cooler.')
        elif output_list[0] == 'Cherry' or output_list[1] == 'Cherry' or output_list[2] == 'Cherry':
            user1.money += 1
            self.money -= 1
            print('+1 credit. Nice. Popped a cherry AND got your money back!')
        elif output_list[0:] == 'Seven':
            user1.money += 10
            self.money -= 10
            print('+10 credits. Lucky for some, and that sum is your bank account.') 
        elif output_list.count('Seven') == 2:
            user1.money += 5
            self.money -= 5
            print('+5 credits. Lady Luck has her eye on you!')
        elif output_list[0:] == 'Bell':
            user1.money += 20
            self.money -= 20
            print('+20 credits. Liberty Egalité! /n That\'s how it goes, right?')
        elif output_list[0:] == 'WIN':
            user1.money += 50
            self.money -= 50
            print('+50 credits. OH WE\'VE GOT THEM BIG BUCKS!')
        else:
            print(random.choice(nope_list))
        return ' '

slots1= Slots()

user1 = User()

user1.name = input('Hey there, what\'s your name? ')
print('Well hi, {name}!'.format(name = user1.name))
print('You\'ve got {money} credits right now.'.format(money = user1.money))

while True:
    play = input('Wanna play the slots? Type yes if you do. ').lower()

    if play == 'yes' or play == 'yes.' or play == 'yep':
        result = slots1.slot_time() 
        print(result)

        if user1.money == 5:
            keep_going = input('Easy tiger, wanna keep going? ').lower()
            if keep_going in ['yes', 'yes.', 'yep']:
                result = slots1.slot_time() 
                print(result)

        if user1.money == 2:
            getting_close = input('You\'re almost out. Only 2 credits left. You sure you wanna keep going? ')
            if getting_close in ['yes', 'yes.', 'yep']:
                result = slots1.slot_time() 
                print(result)

        if user1.money == 1:
            almost_done = input('One left. Want to risk it? ')
            if almost_done in ['yes', 'yes.', 'yep']:
                result = slots1.slot_time() 
                print(result)

        if user1.money == 0:
            print('You\'re all out. I think we\'re done here.')
            print('Unless...')
            borrow = input('Wanna borrow more? ')
            if borrow in ['yes', 'yes.', 'yep']:
                user1.money += 10
                print('Alright.')
                print('You have {amount} credits left.'. format(amount = user1.money))
    else:
        print('Fair enough, come back when you\'re ready.')
        break

print('You have {amount} credits. See you again.'. format(amount = user1.money))


