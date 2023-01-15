# 1
# string_data=input("enter your string")
# d={}
# for ch in string_data:
#     d[ch]=d.get(ch,0)+1
# for key,value in d.items():
#     print(key,'occurs', value, 'time')
# 
# 

# 2
# i= input("enter your string :")
#
# d={}
#
# for ch in i:
#     if ch in d:
#         d[ch]+=1
#     else:
#         d[ch]=1
# print(d)

# 3

# from collections import Counter
#
# i= input("enter the string")
#
# count= Counter(i)
#
# print(count)


#338. Counting Bits

# Given an integer n,
#  return an array ans of length n + 1 such that for each i (0 <= i <= n),
#  ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# logic is very simple if number is even it will be  (n/2)  if odd (n/2)+1 
# like m[0] = 0 , m[1]= m[1/1] +1 =m[0]+1=1 ,m[2] = m[2/2]= m[1]=1 , m[3] = m[3//2]+1 = m[1]+1 = 2 
# def countBits(n: int):
#     # first create array of n+1 lenth with 0 as intinial
#         m=[0]*(n+1)
#         #first element will be zero 
#         m[0]=0
#         for i in range(0,n+1):
#             m[i] = m[i//2] +i%2
#         return m    
# n=2
# print(countBits(n))










# string = "Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer to this as the “controlling idea,” because it controls what happens in the rest of the paragraph."

# d= {}

# for ch in string:
#     if ch in d:
#         d[ch]+=1
#     else:
#         d[ch]=1           
# print(d)


# Derived class, base_1 class, and base_2 class. The derived class should inherit base_1 and base_2 classes. 
# Any derived class object created should be initiated with 2 variables - a,b. Any base_1 
# class object created should be initiated with variable a and base_2 class object should be initiated
#  with variable b. On creating a base_1 class object, a new variable c should be attributed to the 
#  object with the value 5*a. On creating a base_2 class object, a new variable d should be attributed
#   to the object with the value 10*b. Write a python program to create a derived
# class object with a=2,b=3 and print the 2 new variables (c,d) created.








