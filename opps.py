'''

Abstraction: Hiding Complexity

Abstraction is the process of hiding unnecessary details and exposing only essential features of an object or system.
It allows developers to focus on high-level functionality without getting lost in the implementation details. 
Abstraction is achieved through abstract classes and interfaces in Python.
An abstract class is a blueprint for other classes and cannot be instantiated itself. 
It defines common attributes and methods that subclasses must implement.
By defining an abstract class, we can ensure that subclasses adhere to a certain structure or behaviour.

'''

# inheritance 
# abstraction
# polymorphisam 

# abstraction


from abc import ABC,abstractmethod


class Vehicle(ABC):



    @abstractmethod
    def start(self):
        pass




class Audi(Vehicle):
    def __init__(self) -> None:
        pass

    def start(self):
        pass

    def go(self):
        print("going ....")


a = Audi()

# a.go()


# overriding 

class Animal:

    def speak(self):
        print("Animal Speak")


class Tiger(Animal):

    def speak(self):
        print("Roar")



def call_speak(obj):
    return obj.speak()



# a = Animal()
# call_speak(a)


# overloading 


class Person :


    def make_sum(self,a=None,b=None,c=None):
        s= 0
        if a!= None and  b!= None and  c!= None:
            s = a+b+c

        elif a!= None and  b!= None:
             s = a+b
        else:
            s=a
        return s



p = Person()

# print(p.make_sum(1,56,))





# encapsulation  


class Person:
    
    def __init__(self,name,age):
        self.__age = age    # private
        self.__name = name   # private
 

    def Name(self):
        return self.__name
    
    def age(self):
        return self.__age
    



p = Person("raj",25)
print(p._Person__age)



