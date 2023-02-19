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


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        
    def show_balance(self):
        print(f'{self.name}, has an account balance of: {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.name, self.balance
        else:
            print('Insufficient funds')
    
    def deposit(self, amount):
        self.balance += amount
        return self.name, self.balance
    
    def transfer_money(self, amount, pin):
        if self.pin != pin:
            return False
        elif self.pin == int(input('Enter your pin: ')) and self.balance >= amount:
            self.balance -= amount
            self.balance += amount
            print(f'You are transferring {amount} to {user1.name}')
            return True
        else:
            print('Insufficient balance.')
            return False
            
    
    def request_money(self, amount, password, pin):
        if self.pin != pin or self.password != password:
            return False
        else:
            self.balance += amount
            return True


""" Driver Code for Task 5"""

user1 = BankUser('Bob', 1234, 'password')
print(user1.name, user1.pin, user1.password, user1.balance)

user2 = BankUser('Ryan', 4321, 'password1234')
print(user2.name, user2.pin, user2.password, user2.balance)

user2.deposit(5000)
user2.show_balance()
user1.show_balance()

if user2.transfer_money(500, 4321):
    user1.request_money(50, 'password1234', 1234)

user1.show_balance()
user2.show_balance()