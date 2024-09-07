# import pandas as pd


# list1  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even = list(filter(lambda x: x%2!=0,list1))

# print(even)


# list1 = [5, 3, 5, 2, 1, 6, 6, 4]

# # unique = set(list1)
# unique = []
# dublicate =[]
# for i in list1:
#     if i not in unique:
#         unique.append(i)
#     else:
#         dublicate.append(i)

# unique = [u for u in unique if u not in dublicate]

# word = "my name is ranajoy"

# reverse = (' ').join(word.split()[::-1])
# print(reverse)


# def febo():
#     a=0
#     b=1
#     while True:
#         yield a
#         a,b = b,a+b

# f=febo()

# print(next(f))
# print(next(f))

# def febo(n):
#     a=0
#     b=1
#     if n==0:
#         return 0
#     elif n ==1 or n==2:
#         return 1
#     else:
#         for i in range(1,n):
#             a,b=b,a+b
#         return b
    
# for i in range(0,11):
#     print(f"index of {i} with fibonacci series {febo(i)}")    



#3 Palindrome number
# num=121  ==> 1 => 7*10 =10+ 2 =12=>12*10 +1 =121
# def palindrome(num):
#     rev = 0
#     check = num
#     while num>0:
#         rev = (10*rev) + (num%10)
#         num = num//10
#     if check == rev:
#         print("palindrome")
#     else:
#         print("not palindrome")

# palindrome(199)        

#4 Palindrome string

# def palindrome(s):
#     rev =""
#     for i in range(len(s)-1,-1,-1):
#         rev=rev+s[i]
#     if rev == s:
#         print("palindrome")
#     else:
#         print("not palindrome")

# palindrome("rar")

# decorator

# def decorator(func):
#     def wrapper(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return wrapper

# @decorator
# def div(a,b):
#     print (a/b)
# div(2,8)

# 2) find the sum of each string and find the biggest sum from the list
# A=[222,121,145,611] find the largest sum if entire number ,
# like 2+2+2=6 ,1+2+1= 4

# arr =[124,341,126,632]

# new=[]
# for i in arr:
#     string= list(map(int,str(i)))
#     add = sum(string)
#     new.append(add)
# max_value = max(new)
# print(max_value)    



#sort without using sort Keyword 
# list = [-5, -23, 5, 0, 23, -6, 23, 67]

#1) time-complexity = o(n2)
# for i in range(len(list)):
#     for j in range (i+1,len(list)):
#         if list[i]>list[j]:
#             list[i],list[j] = list[j],list[i]
# print(list)

#2) time-complexity = o(n)
# new_list=[]
# while list:
#     min = list[0]
#     for i in list:
#         if min>i:
#             min = i
#     new_list.append(min)
#     list.remove(min)
# print(new_list)        





# print all the pairs with given sum

# list=[8,7,2,5,3,1]
# sum = 10

# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]+list[j] == sum:
#             print(f"value of {list[i]} and {list[j]} with index of {list.index(list[i])} and {list.index(list[j])} compraised the {sum}")

# l=[]
# for i in list:
#     temp = sum - i
#     if temp in l:
#         print(temp,i)
#     l.append(i)    

# file = pd.read_csv('Sample.csv',encoding= 'unicode_escape')

# print(file.loc[:, "3":"Nunavut"])


# def febo(n):
#     a=0
#     b=1

# #     while True:
# #         yield a
# #         a,b = b, a+b

# # feb =febo()

# # print(next(feb))
# # print(next(feb))
# # print(next(feb))
# # print(next(feb))
# # print(next(feb))
# # print(next(feb))

#     if n == 0:
#         return 0
#     elif n ==1 or n ==2:
#         return 1

#     else:
#         for i in range(1,n):
#             a,b=b,a+b
#         return b    
    
# for i in range(0,11):
#     print(f"index of {i} with febonaci series {febo(i)}")    



# list = [-5, -23, 5, 0, 23, -6, 23, 67]

# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]>list[j]:
#             list[i],list[j] = list[j],list[i]
# print(list)        


# list=[8,7,2,5,3,1]
# sum = 10






# def decorator(fun):
#     def wrapper(a,b):
#         if b>a:
#             return fun(b,a)
#     return wrapper 


# @decorator
# def div(a,b):
#     print(a/b)

# div(2,4)

#Output: [0, 1, 4, 9, 9, 16, 16, 25, 25]
# Input =[-5, -4, -3, -1, 0, 2, 3, 4, 5]

# def sort(n):  # sourcery skip: avoid-builtin-shadow
#     list_1 = [ i*i for i in n]
#     new_list_1=[]
#     while list_1:
#         min= list_1[0]
#         for i in list_1:
#             if i< min:
#                 min = i
#         new_list_1.append(min)
#         list_1.remove(min)        
#     print(new_list_1)    

# sort(Input)    


# list1=[8,7,2,5,3,1]
# sum = 10

# new=[]
# for i in list:
#     left = sum-i
#     if left in new:
#         print(i,left)
#     new.append(i)

# even = list(filter(lambda x:x%2!=0,list1))
# print(sorted(even))





Input =[-5, -4, -3, -1, 0, 2, 3, 4, 5]


def sort_fun(arr):
    new_arr = []
    while arr:
        max_value=arr[0]
        for i in arr:
            if i > max_value:
                max_value = i
        new_arr.append(max_value)
        arr.remove(max_value)
    print(new_arr)
sort_fun(Input)