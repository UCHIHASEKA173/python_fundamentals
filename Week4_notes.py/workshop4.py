class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin 
        self.password = password

    def change_name(self, new_name):
        self.name = new_name


    def change_pin(self, new_pin):
        self.pin = new_pin 

    def change_password(self, new_password):
        self.password = new_password


class BankUser:
    def __init__(self, name, pin, password):
        super().__init__()
        self.name = name
        self.pin = pin
        self.password = password
        self.balance = 0
        
    def show_balance(self):
        print(f'{self.name}, has an account balance of: {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.name, self.balance
        else:
            print('Insufficient funds')
    
    def deposit(self, deposit):
        self.balance += deposit
        return self.name, self.balance
    
    def transfer_money(self, amount, pin):
        print('You are transferring $500 to Bob.')
        print('Authentication Required.')
        sender_pin = int(input('Enter pin: '))    
        if self.pin == sender_pin and self.balance >= amount:
            self.balance -= amount
            self.balance += amount
            return True
        elif sender_pin != self.pin:
            print('Invalid Pin, Transfer Cancelled.')
            print(user2.showbalance())
            print(user1.showbalance())
            return False
        elif self.balance < amount:
            print('Insufficient Balance.')
            print(user2.show_balance())
            print(f'{user1.show_balance()}\n')
            return False
            
    
    def request_money(self, amount, password, pin):
        print('You are requesting $250 from Bob.')
        print('User authentication required...')
        requestor_pin = int(input("Enter Bob's Pin: "))
        user_password = input('Enter your password: ')
        
        if requestor_pin == user1.pin and user_password == user2.password: 
            self.balance -= amount
            self.balance += amount
            return True
        elif requestor_pin != user1.pin:
            print('Invalid Pin, Transfer cancelled')
            print(user2.show_balance())
            print(f'{user1.show_balance()}\n')
            return False
        elif user_password != user2.password:
            print('Invalid password. Transfer cancelled.')
            print(user2.show_balance())
            print(f'{user1.show_balance()}\n')
            return False
        else:
            return False



            






      

""" Driver Code for Task 1 """

'''

user1 = User('Bob', 1234, 'password')
print(user1.name, user1.pin, user1.password')
'''

""" Driver Code for Task 2 """

'''
user1 = User('Bob', 1234, 'password')
print(user1.name, user1.pin, user1.password)

user1.change_name('Bobby')
user1.change_pin(4321)
user1.change_password('newpassword')
print(user1.name, user1.pin, user1.password)
'''





""" Driver Code for Task 3"""
'''
bankuser1 = BankUser('Bob', 1234, 'password')
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)
'''
""" Driver Code for Task 4"""
'''
bankuser1 = BankUser('Bob', 1234, 'password')
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)

bankuser1.show_balance()
bankuser1.deposit(100)
bankuser1.show_balance()
bankuser1.withdraw(50)
bankuser1.show_balance()
'''


""" Driver Code for Task 5"""
'''
user1 = BankUser('Bob', 1234, 'password')


user2 = BankUser('Ryan', 4321, 'password1234')


user2.deposit(5000)
print(user2.show_balance())
print(f'{user1.show_balance()}\n')
user2.transfer_money(500, 4321)

if user2.transfer_money(500, 4321):
        print('Transfer Authorized.')
        print(f'You are transferring $500 to Bob')
        print(f'{user2.withdraw(500)}')
        print(f'{user1.deposit(500)}\n')
        
        if user1.request_money(250, 1234, 'password1234'):
            print('Request Authorized.')
            print(f'{user1.name} sent $250')
            print(f'{user2.deposit(250)}')
            print(f'{user1.withdraw(250)}\n')

'''
