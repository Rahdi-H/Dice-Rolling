import random

def roll_the_dice():
    roll = input('would you like to roll the dice? Yes/No : ')
    while roll.lower() == 'yes':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print('you got : ', dice1, ",", dice2)
        roll = input('would like to roll again? Yes/No : ')

roll_the_dice()