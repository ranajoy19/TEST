# single level inheritance

#       [a]
#        |
#       [b]

# class Parent ():
#     def __init__(self,parent):
#         self.parent = parent

#     def parent_name(self):
#         print("parent name is {}".format(self.parent))

# class Child (Parent):
#     def __init__(self,child,parent):
#         self.child = child 
#         super().__init__(parent)
    
#     def child_name(self):
#         print("child name is {}".format(self.child))
#         print("parent name is {}".format(self.parent))




# child = Child("bablu","chunni")
# child.child_name()


# Multilevel Inheritance :


#       [a]
#        |
#       [b]
#        |
#       [c]

# Base class1
# Base class
 
 
# class Grandfather:
 
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername
 
# # Intermediate class
 
 
# class Father(Grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
 
#         # invoking constructor of Grandfather class
#         Grandfather.__init__(self, grandfathername)
 
# # Derived class
 
 
# class Son(Father):
#     def __init__(self, sonname, fathername, grandfathername):
#         self.sonname = sonname
 
#         # invoking constructor of Father class
#         Father.__init__(self, fathername, grandfathername)
 
#     def print_name(self):
#         print('Grandfather name :', self.grandfathername)
#         print("Father name :", self.fathername)
#         print("Son name :", self.sonname)
 
 
# #  Driver code
# s1 = Son('Prince', 'Rampal', 'Lal mani')
# print(s1.grandfathername)
# s1.print_name()


# Hierarchical Inheritance  

#       [a]
#        /\
#     [b]  [c]
#        
#       
# Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
 
# # Derived class1
 
 
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")
 
# # Derivied class2
 
 
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")
 

# # Driver's code
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()


# class parent:
#     def __init__(self,parent_name):
#         self.parent_name = parent_name

#     def show_parent_name(self):
#         print(f"parent name is {self.parent_name}")

#     def show(self):
#         print("hello world")    

# class child(parent):
#     def __init__(self,child_name ,parent_name):
#         self.child_name = child_name
#         parent.__init__(self,parent_name)

#     def show_name(self):
#         print(f"parent is {self.parent_name} and child is {self.child_name}")


# Child = child("rob","job")
# Child.show_parent_name()


class Parent:

    def __init__(self,parent_name):
        self.parent_name = parent_name

    def display(self):
        print(self.parent_name)

    
class Child(Parent):
    def __init__(self, parent_name,child_name):
        self.child_name = child_name
        Parent.__init__(self,parent_name)

    def display(self):
        Parent.display(self)
        print(self.child_name)


child =Child("raja","chompa")

child.display()