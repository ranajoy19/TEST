# from abc import ABC , abstractclassmethod
# class Student(ABC):

#     school_name = "PR-International"


#     def __init__(self,age,name):
#         self.age = age
#         self.name = name

#     @abstractclassmethod
#     def get_name(self):
#         return f'my name is {self.name} and age is {self.age}'
    
#     # @staticmethod
#     # def check_age(age):
#     #     if age>18:
#     #         print("you are an adult")
#     #     else:
#     #         print("you are a teenager")

    
# class Teacher(Student):
#     def __init__(self,age,name,department):
#         self.department = department
#         super().__init__(age,name)

#     def get_name(self):
#         return f'my name is {self.name} and age is {self.age} with department {self.department} and school name is {self.school_name}'
    
#     # @classmethod
#     # def change_school_name(cls,school_name):
#     #     cls.school_name =school_name

    


# s = Teacher(22,"raja","Bengali")


# # print(s.get_name())





rule_variables = {"STATE":"MH"}
text_string = "<<STATE>>"

def parese_templet_values(text_string,rule_variables):
    for var in rule_variables.keys():
        text_string=text_string.replace(f"<<{var}>>",rule_variables[var])

    return text_string
print(parese_templet_values(text_string,rule_variables))





class Student:
    def __init__(self,st_id,st_name,st_clss,st_mark):
        self.st_id = st_id
        self.st_name = st_name 
        self.st_clss = st_clss 
        self.st_mark = None
        self.set_mark(st_mark)
        self.validate()

    @property
    def mark(self):
        return self.st_mark
    

    # @mark.setter 
    def set_mark(self,value):
        if self.st_mark is None:
            if value<0:
                raise ValueError("cant be negetive")
            self.st_mark = value
        else:
            print("Mark is already set and cannot be changed")

    def validate(self):
        if int(self.st_clss) > 12 or int(self.st_clss) < 6:
            print("class can't be greater than 12 or less than 6")
    

s1 =Student("01","na",12,50)
# print(s1.st_mark)



# use db;

# select st_name,parent_id from Student group_by parent_id ;


# bd = artclass(student_id,st_name,parent_id)  examle =  1 , "abc" , 10
#                                                      10 , "bc" , null
 

# select st_name from artclass where parent_id in (select student_id from artclass where parent_id is null) group_by parent_id ;

# s1 = Student("01","akash",13,-50)
# s1.__st_mark = 50 







# s = frozenset([1,2,4,5])

# s1 = list(s)

# s1.append(6)

# new_set = frozenset(s1)
# print(new_set)

# second lasgest element (first and the last)












    