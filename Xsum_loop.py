'''
A while loop that asks the user to enter two numbers.
The numbers are added and the sum displayed.
The loop asks the user if they want to perform another 
operation and if so, repeats. Otherwise terminates.
'''


while True:
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    sum = int(num1) + int(num2)
    print(sum)
    again = input('Do you want another set Y or N?: ')
    if again == 'N':
        break
    elif again == 'Y':
        continue
    else:
        break