# file=open(r'E:\joy\The Python Mega Course Build 10 Real World Applications\[Tutsgalaxy.com] - The Python Mega Course Build 10 Real World Applications\06 File Handling\054 example.txt'
#           ,'r+')
# file.write('line 4\n')
# context=file.read()
# print(context)

# marge dictionary

#dict1={'1':'orange','2':'mango'}
#dict2={'3':'banana','4':'guava'}
# #dict3={**dict1,**dict2}
# #print(dict3)
#
#dict1.update(dict2)
#print(dict1)

# Remove Duplicates from List?

# arr=[1,2,3,4,5,1,2,3,4,5,6,7,8,4,5]
# arr1=[]
# for i in arr:
#     if i not in arr1:
#         arr1.append(i)
# print(arr1)

# using dictionary
# dict1 = {'1': ['orange','mango','mango','banana','orange']}
#
# dict3={}
# for key,value in dict1.items():
#     dict3[key]=set(value)
# print(dict3)

# #maximum difference in two element

# arr=[ 5,32 ,45,4,12,18,25]

# arr.sort()
# max = 0.000001
# for i in range(len(arr)-1):
#     if max< (arr[i+1]-arr[i]):
#         max= arr[i+1]-arr[i]
# print(max)

#finding the non repeating number
# from collections import Counter
#
#nums = [1,3,4,2,2,3,1,4,5]
# fre = Counter(nums)
# print(fre)
# for i in nums:
#     if fre[i] ==1:
#         print(i)

#
# def febo(n):
#
#     a=0
#     b=1
#     if n==1 or n==2:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         for i in range(1,n):
#
#
#             return febo(n-1)+febo(n-2)
#         #     c =a+b
#         #     a=b
#         #     b=c
#         # return b
#
# for n in range(1,13):
#     print(n,febo(n))




