## simple function with docstring
def my_function(param1='default'):
    """
    PRINTS OUT A LITTLE TEXT AND THEN THE INPUT / DEFAULT
    OUTPUT IS THE INPUT / DEFAULT BACKWARDS
    """
    print("this is my first python function: {}".format(param1))
    return param1[::-1]

output = my_function('something')
print(output)

## check if input is as expected
def addNum(num1, num2):
    """
    If input is int, returns their sum
    Else prints error
    """
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    else:
        print('at least one of the inputs is not an integer')

print(addNum(1,2))
addNum('abc', 3)

## using function as filter
my_list = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool,my_list)
print(list(evens))

## as lambda
evens = filter(lambda num: num%2 == 0, my_list)
print(list(evens))

## split function
tweet = 'Go Sports! #sports'
result = tweet.split('#')
print(result)

## in function
print('x' in [1,2,3])
print('x' in [1,2,'x'])
