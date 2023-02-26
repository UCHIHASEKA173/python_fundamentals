import random

def guess_random_number(tries, start, stop):
    target = random.randint(start, stop)
    while tries != 0:
        print(f'You have {tries} tries remaining.')
        guess = input('Enter your guess: ')
        
        if target == int(guess):
            print('Correct guess!')
            return True
            break 
        if target >= int(guess):
            print('Guess higher')
            tries = tries - 1
        if target <= int(guess):
            print('Guess lower')
            tries = tries - 1
        if tries == 0:
            print(f'You failed to guess the number {target}.')
            break

        
#guess_random_number(5, 0, 10)  

def guess_random_num_linear(tries, start, stop):
    target = random.randint(start, stop)
    print(f'The number for the program to guess is {target}.')
    for i in range(start, stop):
        tries -= 1
        
        print(f'Number of tries left: {tries}')
        if i == target:
            print(f'The program is guessing {i}.')
            print('The program guessed correct!')
            return 
        elif i < target and tries > 0:
            print(f'The program is guessing {i}.')    
        elif i > target and tries > 0:
            print(f'The program is guessing {i}.')    
        elif tries < 1:
            
            print(f'The program has failed to guess the number {target}')
            return 
        
    

#guess_random_num_linear(6, 0, 10)

def guess_random_num_binary(tries, start, stop):
    target = random.randint(start, stop)
    print(f'The program is trying to find {target}.')
    low, high = start, stop
    while low <= high and tries > 0:
        guess = low + high // 2
        if guess == target:
            print(f'Found it! {target}')
            return
        elif guess < target and tries > 0:
            low = guess + 1
            print('Guessing higher')
        else:
            high = guess - 1
            print('Guessing lower')
        tries -= 1
    print('The program failed to guess the number')

#guess_random_num_binary(5, 0, 100)

        

