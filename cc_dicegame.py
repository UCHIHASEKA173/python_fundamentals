import random

high_score = 0


def dice_game():
    while True:
        global high_score
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        total = die_2 + die_1
        print(f'Current high score: {high_score}' )
        print('1) Roll Dice')
        print('2) Leave Game')
        choice = input('Enter your choice: ')
        if choice == '1':
            print(f'You roll a... {die_1}')
            print(f'You roll a... {die_2}')
            print(f'You have rolled a total of: {total}')
            print('\n')
        if total > high_score:
            high_score = total
            print('New high score!')
        if choice == '2':
            print('Goodbye')
            break





dice_game()
