'''
a = input('What is your name? ')
print('Your name is ' + a)
b = input('What is your address with city state and zip? ')
print('Your address is ' + b)
c = input('What is your phone number? ')
print('Your number is ' + c)
d = input('What is your college degree? ')
print('Your degree is ' + d)
'''
#Land calculator
'''
acre = 43_560
total_square_feet = input('How many square feet of land do you own ')
total_square_feet = int(total_square_feet)
total_acreage = (total_square_feet / acre)
print('You own ' + str(total_acreage) + ' acres')
'''

#Total purchase
'''
sales_tax = 0.07
sub_total = 0
a = input('What is the price of the shirt? ')
a = float(a)
sub_total += a 
b = input('What is the price of the pants? ')
b = float(b)
sub_total += b
c = input('What is the price of the jacket? ')
c = float(c)
sub_total += c
d = input('What is the price of the shoes? ')
d = float(d)
sub_total += d
e = input('What is the price of the hat? ')
e = float(e)
sub_total += e
print('Subtotal: $' + str(sub_total))
print('Sales tax: 7%' )
sub_total = float(sub_total)
total_sales_tax = (sub_total * sales_tax) 
total = sub_total + total_sales_tax
print('Total: $' + str(total))
'''
day = input('What number day of the week is it? ')
day = int(day)
if day >= 7:
    quit
if day == 1:
    print('Today is Sunday. ')
if day == 2:
    print('Today is Monday. ')
if day == 3:
    print('Today is Tuesday. ')
if day == 4:
    print('Today is Wednesday. ')
if day == 5:
    print('Today is Thursday. ')
if day == 6:
    print('Today is Friday. ')
if day == 7:
    print('Today is Saturday. ')





