'''
A while loop that lets the user enter a number. 
The number is multiplied by 10, and the result 
assigned to a variable named product. The loop will 
iterate as long as the product is less than 100.
'''



while True:
    product = input("Enter a number: ")
    product = int(product) * 10
    if product < 101:
        print(product)
