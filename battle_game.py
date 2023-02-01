'''
  Please see below for my comments marked as --##--
'''

wizard = "Wizard"
elf = "Elf"
human = "Human"
wizard_hp = 70
elf_hp = 100
human_hp = 150
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_hp = 300
dragon_damage = 50
print(f'1 {wizard}')
print(f'2 {elf}')
print(f"3 {human}")

character = input('Choose your character:')
while True:
    # --##-- You are close. It should be character != '1' or character != '2' or character != '3'
    if character != '1' or '2' or '3':  # This if statement will cause some bugs in your code.
        print('Unkown character.')
        character = input('Choose your character:')
    if character == '1':
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == '2':
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == '3':
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    
    
    
print(f'You have chosen: {character}')
print(f'Health: {my_hp}')
print(f'Damage: {my_damage}')
while True:
    dragon_hp = dragon_hp - my_damage
    if dragon_hp <= 0:
        print('The dragon has lost the battle!')
        break
    print(f'The {character} damaged the dragon.')
    print(f'The dragons health is now: {dragon_hp}')
    my_hp = my_hp - dragon_damage
    if my_hp <= 0:
        print('You have lost the battle.')
        break
    print(f'The dragon has damaged the {character}')
    print(f'The {character}s health is now {my_hp}.')





