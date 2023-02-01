def myFn():
    print('You have called my function')

def add(x, y):
    return x + y
   

myFn()
add(2, 3)
add(3, 4)
a = 4
v = 5
add(a, v)

def a_function(callback):
    print(callback(3))

a_function(lambda num : num ** 2)
lambda num: num ** 2

