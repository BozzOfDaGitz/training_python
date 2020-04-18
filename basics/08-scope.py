## SCOPE

# x = 25
#
# def my_func():
#     x = 50
#     return x
#
# print(my_func())
# print(x)

## LOCAL

# lambda x: x**2

## ENCLOSING FUNCTION LOCALS

# name = 'This is a global name!'
#
# def greet():
#     name = 'Sammy'
#
#     def hello():
#         # name = 'Henry'
#         print('Hello ' + name)
#
#     hello()
#
# greet()
# print(name)

## GLOBAL

# x = 50
#
# def func():
#     global x
#     # print('x is:',x)
#     x = 1000
#     print('global x changed to:',x)
#
# print('before function, x is: ',x)
# func()
# print('after function call, x is: ',x)
