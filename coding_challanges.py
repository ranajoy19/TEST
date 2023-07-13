# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.

# l = [
#     ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
#     ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
#     ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
#     ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
#     ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
#     ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
#     ]

# # List of participants who participated daily
    
# # res1=list(set.intersection(*map(set,l)))
# # print(res1)

# class code:
#     def __init__(self,l):
#         self.l=l
#         self.l1=[]
#         self.d={}
#         self.res1=[]
#         self.res2=[]
#         self.res3=[]
#     def helper(self):
#         for i in l:
#             for j in i:
#                 self.l1.append(j)
#         self.d={i:self.l1.count(i) for i in self.l1}
#         return self.d
        
# # List of participants who participated daily
    
#     def case1(self):
#         d=self.helper()
#         for k,v in d.items():
#             if d[k]==6:
#                 self.res1.append(k)
#         return(self.res1)    

# # List of participants who participated only once    
#     def case2(self):
#         d=self.d
#         for k,v in d.items():
#             if d[k]==1:
#                 self.res2.append(k)
#         return(self.res2)

# # List of participants who participated on the first day and never participated again.

#     def case3(self):
#         first_day=l[0]
#         for i in l[0]:
#             if i not in l[1]+l[2]:
#                 self.res3.append(i)
#         return(self.res3)             
    
# Code=code(l)
# print(Code.case1())
# print(Code.case2())
# print(Code.case3())


    
    
    
# # res1=[]
# # # List of participants who participated only once
# # res2=[]
# # l1=[]
# # for i in l:
# #     for j in i:
# #         l1.append(j)

# # d={i:l1.count(i) for i in l1}
# # for k,v in d.items():
# #     if d[k]==1:
# #         res2.append(k)
# #     elif d[k]==6:
# #         res1.append(k)
# # # print(res1)
# # # print(res2)
# # print(d)

