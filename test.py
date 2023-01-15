#Fibonacci series

'''def Fibonacci(n):
    a=0
    b=1
    if n==1 or n==2:
        return 1
    elif n ==0:
        return 0

    else:
        #return Fibonacci(n - 1) + Fibonacci(n - 2)
        for i in range(1,n):

            c=a+b
            a = b
            b=c
        return b

# Driver Program
for n in range(1,11):
    print(n ,":" ,Fibonacci(n))

'''

# second largest element in the list
#
# list=[10,40,70,50,100]
#
# list.sort()
#
# print("Second largest element in the list is :",list[-2])
#
#
# find te common letters between two string

# string1= 'naina'
# string2= 'rene'
#
# s1=set(string1)#droping the duplicates
# s2=set(string2)#droping the duplicates
#
# common = s1 & s2
# print(s1,s2)
# print(common)

# write a program to convert a two list into dictionary and tuple
# list1=['naina','kimi','sheena']
# list2=[85666,73444,90000]
# # list to dictinary
# dic=dict(zip(list1,list2))
# # dictionary to tupple
# for i in dic.items():
#     print(i)

# finding missing number in the array (submission method and Xor Operation)
#1)
# array=[1,2,4,5,6,7]
# n= len(array)
# total_sum= (n+1)*(n+2)/2
#
# print(total_sum-sum(array))

# Find Out Pairs with given sum in an array in python of time complexity O(n log n)
#
# arr=[5,7,4,3,9,8,19,21]
# sum=17
#
# l=[]
#
# for i in range(len(arr)):
#     left=sum-arr[i]
#     if left in l:
#         print(arr[i],left,)
#     l.append(arr[i]) #[5,7,4,3,9,8]
#     print(l)
#
# Find minimum difference between two elements of Binary Tree

#
# arr.sort()
#
# min_difference= 999*99
#
# for i in range(len(arr)-1):
#     if min_difference> arr[i+1]-arr[i]:
#         min_difference=arr[i+1]-arr[i]
# print(min_difference)


# Find maximum difference between two elements of Binary Tree

#arr=[ 5,32 ,45,4,12,18,25]


# arr.sort()
# print(arr)
# max_diff= 0.00001
#
# for i in range(len(arr)-1):
#     if max_diff< arr[i+1]-arr[i]:
#         max_diff = arr[i + 1] - arr[i]
# print(max_diff)


#finding the non repeating number
# from collections import Counter
#
# #nums=input()
# nums = [1,3,4,2,2,3,1,4,5]
# frequency=Counter(nums)
#
# for i in nums:
#     if (frequency[i]==1):
#         print(i)

#find duplicate number from the list

# nums = [1,3,4,2,2]
#
# n=[]
# for i in nums:
#     if i in n:
#         print(i)
#     else:
#         n.append(i)

# LAMDBA FUNCTION
# x=lambda a: a*a
# print(x(3))

#list
# list=['rana',9,'mona','sonu']
#
# #list[3]='raja'
# list.extend(['raja','sonu'])
#
# print(list)


#Even Pairs

# def even_pairs(A):
#     n=len(A)
#     i=0
#     while(i<n):
#         num=''
#         count=0
#         while i<n and ord(A[i])>=ord('0') and ord(A[i])<=ord('9'):
#             num+= A[i]
#             temp=int(num)
#
#             if temp%2 ==0:
#                 print(num)
#                 num= ''
#                 count+=1
#             i+=1
#         if count >=2:
#             return True
#         i+=1
#
#     return False
#
# print(even_pairs('f09r27i8e67'))


# age count
#
# import requests
#
# result = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
#
#
# print(result.json())
#
# data = result.json()['data'].split(',')
#
# count =0
# for datas in data:
#     split_data =datas.split('=')
#     if split_data[0].strip() == 'age' and int(split_data[1]) >=50:
#         count+=1
# print(count)

# import re
# def FormattedNumber(strArr):
#
#     number_format= re.compile(r'^\d{1,3}([ ,]?\d{3})*([.,]\d+)?$')
#     if number_format.match(strArr):
#
#         return True
#     return False
# # keep this function call here
#
# print(FormattedNumber("0.232567"))
#


#list comprehensive

# sqaure =[i**2 for i in range(1,101)]
# print(sqaure)


#Subarray with given sum
# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements
# from 2nd position to 4th position
# is 12.

# def subArraySum( arr, n, s):
#     dict = {}
#     cur_sum = 0
#     for i in range(n):
#         cur_sum = cur_sum + arr[i]      # add cur_sum with arry element
#         if cur_sum == s:                #if its cur_sum = total sum stop it print the index
#             return i
#         if (cur_sum - s) in dict:        #if cur_sum extend than total sum (total-cur_sum) = whatever if it will be on the dict remove and add +1 to it
#             return (dict[cur_sum - s] + 2, i + 1)
#         dict[cur_sum] = i
# arr = [1,2,3,7,5]
# n=5
# s=12
# print(subArraySum(arr,n,s))


# # lamda funtion
#
# x = lambda a,b,c: a+b+c
# print(x(2,3,4))



from datetime import date

from datetime import timedelta
Begindatestring = date.today()
print(Begindatestring)
real = Begindatestring+ timedelta(days=365)
print(real)