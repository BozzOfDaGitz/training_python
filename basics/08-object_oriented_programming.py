# print(type([]))
# print(type(()))
# print(type(''))

# class Sample():
#     pass
#
# x = Sample()
# print(type(x))

## CLASS ATTRIBUTES AND METHODS
# class Dog():
#     """
#     Dogs have names and breeds.
#     """
#     ## CLASS OBJECT ATTRIBUTE
#     species = 'mammal'
#
#     ## INITIALIZE CLASS METHOD
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed
#
#
#
# my_dog = Dog('Claude','Doggo')
# print(type(my_dog))
# c_name = my_dog.name
# c_breed = my_dog.breed
# c_species = my_dog.species
# print('{} is a {}. As all other dogs, {} is a {}.'.format(c_name,c_breed,c_name,c_species))

## MORE METHODS AND ATTRIBUTES
# class Circle():
#     pi = 3.14
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     def area(self):
#         return self.radius**2 * Circle.pi
#
#     def set_radius(self, new_r):
#         self.radius = new_r
#
#
#
# my_c = Circle(3)
# print(my_c.radius)
# print(my_c.area())
# my_c.radius = 10
# print(my_c.radius)
# print(my_c.area())
# my_c.set_radius(100)
# print(my_c.radius)
# print(my_c.area())

## INHERITANCE
# class Animal():
#
#     def __init__(self):
#         print('ANIMAL CREATED')
#
#     def who_am_i(self):
#         print('ANIMAL')
#
#     def eat(self):
#         print('EATING')
#
# class Carnivore(Animal):
#
#     def __init__(self):
#         # Animal.__init__(self)
#         print('CARNIVORE CREATED')
#
#     def bark(self):
#         print('ROAR!')
#
#     def eat(self):
#         print('EATING MEAT!')
#
# anim = Animal()
# anim.who_am_i()
# anim.eat()
#
# carn = Carnivore()
# carn.who_am_i()
# carn.eat()
# carn.bark()

## SPECIAL
class Book():

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{} written by {}'.format(self.title,self.author)

    def __len__(self):
        return len(self.title) + len(self.author)

    def __del__(self):
        print('a book is destroyed!')
        del self

my_list = [1,2,3]
print(my_list)

my_book = Book('FACTFULNESS','HANS ROHLING')
print(my_book)
print(len(my_book))
del my_book
print(my_book)
