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
# 
# cache={}
# def febo(n):
#     if n in cache:
#         return cache[n]
#     if n == 0:
#         return 0
#     if n ==1 or n==2:
#         cache[n] = 1
#     else:
#         cache[n] =febo(n-2)+febo(n-1)

#     return cache[n]




# for i in range(1,51):
#     print(i,"==>",febo(i))

# s = "my name is ranajoy"
# result = " ".join(s.split()[::-1])
# print(result)


# def palindrome(n):
#     rev = ""
#     for i in range(len(n)-1,-1,-1):
#         rev = rev + n[i]
#     if rev == n:
#         return(f"{n} is a palindrome")
#     else:
#         return(f"{n} is a not palindrome")

# print(palindrome("515"))

# n = 153 => 1^3 * 5^3 * 3^3 
#            = 1 + 125 + 27 = 153


# def armstrong(n):
#     org = n 
#     rev = 0
#     s = len(str(n))
#     while n>0:
#         d = n % 10
#         rev += (d**s)
#         n = n//10
#     if org == rev :
#         return (f"{rev} is armstrong number")
#     else:
#         return (f"{rev} is  not a armstrong number")    
# print(armstrong(153))


# like 2+2+2=6 ,1+2+1= 4

# arr =[124,341,126,632]

# # for i in arr:
# # element =list(map(str,arr))
# result =[] 
# for i in arr:
#     element =list(map(int,str(i)))
#     result.append(sum(element))

# print(max(result))
    


#sort without using sort Keyword 
# list = [-5, -23, 5, 0, 23, -6, 23, 67]

# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]<list[j]:
#             list[i],list[j] = list[j],list[i]
# print(list)


# print all the pairs with given sum
# lis=[8,7,2,5,3,1]
# s = 10

# def pairs(l,s):
#     check =[]
#     for i in l:
#         left = s-i
#         if left in check:
#             return(l.index(i),l.index(left))
#         check.append(i)

# print(pairs(lis,s))



#Input: s = "aaabbb"
# Output: true
# Explanation:
# The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
# Hence, every 'a' appears before every 'b' and we return true.

# def check(s):
#     b = False
#     for i in s:
#         if i == "a":
#             if b == True:
#                 return False
#         else:
#             b = True
#     return True

# print(check("aaab"))


# Write a Python program to find the common elements between two lists.
# list1=[20,10,30,40,40]
# list2=[30,20,60,70,80]

# # list3 = [i for i in list1 if i in list2]
# list3 = set(list1).intersection(list2)
# print(list3)



# #Write a Python program to find the first non-repeating character in a string.
# string='stststopp'

# def firstUniqChar(s):
#     d = {}

#     for i in range(len(s)):
#         if s[i] in  d:
#             d[s[i]] = True
#         else:
#             d[s[i]] = False

#     for i in range(len(s)):
#         if d[s[i]] == True:
#             return(s[i])


# print(firstUniqChar(string))



# Group Anagrams

# strs = ["eat","tea","tan","ate","nat","bat"]
# # # # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# d = {}
# for i in strs:
#     w = "".join(sorted(i))
#     if w in d:
#         d[w].append(i)
#     else:
#         d[w]=[i]
# print(list(d.values()))


# Remove adjacent duplicate characters from a string
# Input:  AABBBACDDD
# Output: ABACD

# def adjDub(s):
#     res = ""
#     pre = None
#     for i in s:
#         if i!=pre:
#             res+=i
#         pre = i
#     return(res)

# print(adjDub('ABBBBBACDDD'))

# Write a recursive program to reverse a given string.
# Input:  mihup ai
# Output: ia puhim
# def rev(s):
#     length = len(s)
#     if length==0:
#         return 
#     else:
#         last_element = s[length-1]
#         print(last_element,end="")        
#         rev(s[0:length-1])
# rev("mihup ai")

#Is Subsequence - LeetCode


# Input: s = "abc", t = "ahbgdc"
# Output: true

# def Subsequence(s,t):
#     i,j = 0,0
#     while i<len(s) and j< len(t):
#         if s[i] == t[j]:
#             i+=1
#         j+=1    
#     return(i==len(s))
# print(Subsequence('acd','acbgd'))


# 14. Longest Common Prefix
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# def longestCommonPrefix(strs):
#     string = ""
#     for i in range(len(strs[0])):
#         for j in strs:
#             if len(j)==i or strs[0][i] != j[i] :
#                 return(string)
#         string+=j[i]
            
    
# print(longestCommonPrefix(["flower","flow","flight"]))