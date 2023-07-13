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