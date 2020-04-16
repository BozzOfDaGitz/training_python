## AND
(1 < 2) and (2 < 3)

## OR
(1 > 2) or (2 < 3)

## IF, ELIF, ELSE
# if 2<2:
#     print("yes!")
# elif 3<3:
#     print("no!")
# else:
#     print("absolutely not!")

## FOR LOOPS

# seq = [1,2,3,4,5,6]
# for i in seq:
#     print(i)

# d = {"a":1,"b":2,"c":3}
# for item in d:
#     print(item + " : " + str(d[item]))

# mypairs = [(1,2),(3,4),(5,6)]
# for (tup1,tup2) in mypairs:
#     print(tup1)
#     print(tup2)

## WHILE LOOPS

# i = 1
# while i<5:
#     print("{} is {}".format("i",i))
#     i = i+1
# print(str(i) + " is not less than 5!")

## RANGE

# my_range = list(range(0, 21, 2))
# print(my_range)

# for item in range(0, 11, 3):
#     print(item)

## LIST COMPREHENSION

x = [1,2,3,4]

print([num**2 for num in x])
