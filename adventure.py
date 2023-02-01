'''
longsword = 'longsword'
scimitar = 'scimitar'
bow = 'bow'
mage_staff = 'mage staff'
longsword_damage = 100
scimitar_damage = 90
bow_damage = 90
mage = 'mage'
soldier = 'soldier'
stealth = 'stealth'
mage_hp = 150
soldier_hp = 200
stealth_hp = 100

playing = input('Do you want to go on an adventure? ')
if playing.lower != 'yes':
    quit
print('1 scimitar')
print('2 longsword')
print('3 bow')
print('4 mage staff')
answer = input('Pick a weapon ')
scimitar = 1
longsword = 2
bow = 3
mage_staff = 4
if answer == 1:
    print('You have chosen the scimitar.')
if answer == 2:
    print('You have chosen the longsword.')
if answer == 3:
    print('You have chosen the bow.')
if answer == 4:
    print('You have chosen the mage staff.')
else:
    quit
class Adventure:
    def __init__(self):
        self.location = "Starting Room"
'''
print('north, south, east ,or west. ')
def play(self):
    while True:
        print('current location')
        print(f"You are currently in the {self_location}.")
move = input("Where would you like to go? ")
if move == "north":
    self_location = "North Room"
elif move == "south":
    self_location = "South Room"
elif move == "east":
    self_location = "East Room"
elif move == "west":
    self_location = "West Room"
elif move == "quit":
    quit
else:
    print("Invalid move.")

