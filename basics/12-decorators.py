## SCOPE RECAP
# s = 'GLOBAL VARIABLE'
#
# def func():
#     # global s
#     s = 50
#     print(s)
#
# func()
# print(s)

## CALL LOCALS / GLOBALS DICTIONARY
# s = 'GLOBAL VARIABLE'
#
# def func():
#     mylocal = 10
#     print(locals())
#     print(globals()['s'])
#
# func()

## FUNCTIONS WITHIN FUNCTIONS
# def hello(name='Jose'):
#     print('THE HELLO() FUNCTION HAS BEEN RUN!')
#
#     def greet():
#         return 'THIS STRING IS INSIDE GREET()'
#
#     def welcome():
#         return 'THIS STRING IS INSIDE WELCOME()'
#
#     print(greet())
#     print(welcome())
#     print('END OF HELLO()')
#
# hello()
# greet()

## RETURNING FUNCTIONS
# def hello(name='Jose'):
#     print('THE HELLO() FUNCTION HAS BEEN RUN!')
#
#     def greet():
#         return 'THIS STRING IS INSIDE GREET()'
#
#     def welcome():
#         return 'THIS STRING IS INSIDE WELCOME()'
#
#     if name == 'Jose':
#         return greet
#     else:
#         return welcome
#
# print(hello()())
# print(hello('Patrick')())

## FUNCTION AS AN ARGUMENT
# def hello():
#     return 'Hi JOSE!'
#
# def other(func):
#     print('HELLO')
#     print(func())
#
# other(hello)

## CREATE DECORATORS
def new_decorator(func):

    def wrap_func():
        print('CODE HERE BEFORE EXECUTING FUNC')
        func()
        print('FUNC() HAS BEEN CALLED')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('THIS FUNCTION IS IN NEED OF A DECORATOR!')

# func_needs_decorator = new_decorator(func_needs_decorator)


func_needs_decorator()
