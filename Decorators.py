# def decorator_func(func):

#     def wrapper(z):
#         print("wrapper function is working")
#         a =func(2,4) + z
#         print(f"modified sum: {a}")

#     print("decorator function is working")

#     return wrapper(5)

# @decorator_func
# def show(x,y):
#     return x+y

# decorator_func(show)


# @decorator_func
# def show():
#     print("show worked")
#
# show

# labda

# sum =lambda a,b,c,d:a+b+c+d
# print(sum(1,1,1,1))


#list comprehention
# new_list=[i for i in range(10)]
# print(new_list)

#dict comprehention
# dic= {x:x**2 for x in range(10)}
# print(dic)
#
# print(dic[9])


# extrating string number from dict

# d={}]12
#
# name ="wrapper"
#
# for cha in name:
#     if cha in d:
#         d[cha]+=1
#     else:
#         d[cha]=1
#
# print(d)

#
# class person :
#
#     def __init__(self,name):
#         self.name=name
#
#     def say_hello(self):
#         print("my name is "+self.name)
#
#
# class person1(person) :
#
#     def say_bye(self):
#         print("bye "+self.name)
#
#
#
# name1=person1('nitin')
#
# name1.say_bye()


#iterator

# new_list=[4,2,6,6,7,5]
#
# it = iter(new_list)
# print(next(it))
#
# for i in it:
#     print(i)


#generator

# def sqr(n):
#     for i in range(1,n+1):
#
#         yield i*i
# a=sqr(5)
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


#ternary operator

# age =90
# discount = 10 if age<50 else 20
# print(discount)


#list sorting without in-built

#old_list= [11, 3, 7, 5, 2]
# new_list=[]
#
# while(old_list):
#     minimnum = old_list[0]
#     for i in old_list:
#         if minimnum < i:
#             minimnum= i
#     old_list.remove(minimnum)
#     new_list.append(minimnum)
# print(new_list)

#linear search

# def search(n,x):
#
#     for i in range(len(n)):
#         if x== n[i]:
#             print(n.index(x))
#             break
#     else:
#         print("not in the list")
#
# old_list= [11, 3, 7, 5, 2]
# search(old_list,2)
#
#

#Fibonacci series
# def fibo(n):
#     a=0
#     b=1
#     if n ==0:
#         return 0
#     elif (n==1) or (n==2):
#         return 1
#     else:
#         # return fibo(n-1)+fibo(n-2)
#         for i in range(1,n):
#             c=a+b
#             a=b
#             b=c
#             return b
#
# for i in range(1,11):
#     print(i ,fibo(i))


# palindrom number
# def palindrome(n):
#     check = n
#     rev = 0
#     while (n > 0):
#         rev = (rev * 10) + (n % 10)
#         n = n // 10
#     if rev==check:
#         print(rev,'is a palindrome number ')
#     else:
#         print(rev,'is not a palindrome number ')
#
# palindrome(131)









# from collections import Counter
#
# s='pwwkewk'
#
# count =Counter(s)
# print(count)
# for i in count:
#     if count[i]>1:
#         print(i)
#

# for num in range(1,101):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 break
#         else:
#             print(num)





# def decorator_func(func):
#     def wrapper():
#         print(func(4,3))
#         print("wapper funtion is working")
        
#     print("decorator_func is working")
#     return wrapper()
# @decorator_func
# def original_func(a,b):
#     return 'this is my original function',a+b

