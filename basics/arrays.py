# mylist = [1,2,3]
# anotherList = ['stringsadg','1','2','3','23.2','True','asdf',"Abc",'mylist']
# print(anotherList)
#
# anotherList.pop()
#
# print(anotherList[::-1])
# anotherList.reverse()
# print(anotherList)
#
# anotherList.sort()
# print(anotherList)

mylist = [1,2,['x','y','z']]
letters = mylist[2]
y = mylist[2][1]

print(letters)
print(y)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)
