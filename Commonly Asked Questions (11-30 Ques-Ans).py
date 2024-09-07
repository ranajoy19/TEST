#1) Ternary operator
#
# a,b =10,20
# min = a if a<b else b
# print(min)

#2) Inheritance

# 
class A:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("its display")

class B(A):
    def __init__(self, name):
        A.__init__(self,name)
    def show(self):
        print("its show",self.name)


# b= B("raja")

# b.show()
# b.display()


# 3) What is 'self' keyword in python?

# the 'self' Parameter used as a reference to the current instance of class ,and is used to access the variable that \
# belongs to class
#
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#
#         print(f"My name is {self.name}.I am {self.age} years old ")
#
#
# Person = person("raja",45)
#
# Person.info()

#4)Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and
# “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object)
# is converted back into an object hierarchy.

# 5) Iterator An iterator is an object which contains a countable number of
# values and it is used to iterate over iterable objects like list, tuples, sets, etc.

# list= ['Geeks', 'For', 'Geeks']
# iter_list=iter(list)
# print(next(iter_list))
# print(next(iter_list))
# print(iter_list.__next__())

# 5) Generator is an iterator which can be executed one

# def sqe(n):
#     for i in range(1,n+1):
#
#         yield i*i
#
# a=sqe(3)
# print(next(a))
# print(next(a))
#
# print(next(a))


# 6)What does *args and **kwargs mean? explain

# def Sum(*args):
#     total=0
#     for i in args:
#         total=total+i
#     return total
#
# result=Sum(1,2,3,4,5,2,4,5,6)
# print(result)




# def display(**kwargs):
#     return kwargs

# result= display(a=2,b=5,c=10)
# print(result)

# file = open('text.txt','r')

# content = file.read()

# print(content)
# file.close

# with open('text.txt','a+') as f:
#     # pos = f.tell()
#     # pos = pos+2
#     # f.seek(pos)
#     f.write('so maloti ghore ahhi')
  

# with open('text.txt','r') as f:
#     print(f.read())


# 23) what is pythonPath
# => python path is nothing but environmental variable, which has add to setup additional directories , 
# where python look for modules and packages

# dimond problem 
#=>java does not allow multile inheritancs ,where one class can inherite from only one class this is called 
# dimond problem 

# class A:
#     def abc(self):
#         print('a')

# class B():
#     def abc(self):
#         print('b')

# class C():
#     def abc(self):
#         print('c')

# class D(A,B,C):
#     pass

# d=D()
# d.abc()


# what is py and .pyc file 
#=> py files contain the source code of a program. Whereas,
#  . pyc file contains the bytecode of your program.

# Ways to concatenate 2 tuples
# one = (1,2,3) 
# two = (1,2,3)
# print(id(two))
# two = one+two
# print(two)
# print(id(two))

# what is _a ,__a and __a__ in python 

# => _a is protected __a is private key word


class A:
    a=1.5
    _a =2
    __a = 3
    def show(self):
        print(A.a)
    
class B(A):
    def show1(self):
        print(A._a)

# a=A()
# # print(a._A__a)
# a.show()
# b= B()
# b.show1()
# # c= C()
# # print(c.a)       



# api Factor and Standards


# 1) api contract ==> information given by the developer , what endpoint , methods , data o send , formating 
# 2) Documentation => if its public api 
# 3) formating 
# 4) security => ratelimiting and Throttling  

# Standards 

# 1)  RPC 
# 2)  SOAP
# 3)  REST

# session and cookies 

# session is server side and cookies client side

# how to flush the memory on python

# using del and gc.collect()

# from abc import ABC,abstractclassmethod
# # class method and static method 
 
# class vehical(ABC):
    
#     @abstractclassmethod
#     def run(self):
#         pass



    # price =14
    
    # def __init__(self,color,brand) -> None:
    #     self.color =color
    #     self.brand =brand

    # def get_info(self):
    #     print(f"{self.brand} and {self.color}:{self.price}")


    # @classmethod
    # def set_price(cls,price):
    #     cls.price = price


    # @staticmethod
    # def check_age(age):
    #     if age >18:
    #         print("you are an adult")
    #     else:
    #         print("you are a teenager")    
# class car(vehical):
    
#     def run(self):
#         print("car class")

# class bike(vehical):
#     pass 


# # vehical.set_price(100)

# v1 =car()
# v1.run()


# v.get_info()
# v1.get_info()


# vehical.check_age(1)