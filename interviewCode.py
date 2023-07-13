# 1) Two Sum

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


# def AddTwo(nums,target):
#
#     map = []
#     for i in range(len(nums)):
#         left = target - nums[i]
#         if left in map:
#             return (map.index(left), i)
#
#         map.append(nums[i])
#
#
#
# nums = [2,7,11,15]
# target = 9
#
# result=AddTwo(nums,target)
# print(result)

# 2) find the sum of each string and find the biggest sum from the list
# A=[222,121,145,611] find the largest sum if entire number ,
# like 2+2+2=6 ,1+2+1= 4

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


# num=[123,222,785,199,412,666]
# new_num = []
# len(num)
# # print(len(num))
# for i in num:
#     string = list(map(int,str(i)))
#
#     add=sum(string)
#     new_num.append(add)
# print(new_num)
# print(max(new_num))


# 3) Longest Palindromic Substring
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# solution
#  "babad"   right and left as same index like i define than if index is same than we increment right and decrement
# left by one (inside a while loop condition n>=0 and r<len(s)) than see find the difference of r and l by
# lenth = r- l -1 (-1 is important for this logic) , now have to find the start (st) and end position ,in order to
# get that we will see the length difference if it's more than 1 we will set the st and end to the reset position
# of l and r so st= l+1 and end=r-1(because when we do l-1  and r+1 that's give you a plindrome )

# given string

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


# def LPS(s):
#
#     if len(s)<=1:
#         return s
#     max_length=1
#     end,st=0,0
#     n=len(s)
#
#     #for Odd number
#     for i in range(n-1):
#         r=i
#         l=i
#         while(l>=0 and r<n ):
#             if(s[r]==s[l]):
#                 l -= 1
#                 r += 1
#             else:
#                 break
#         length= r-l-1
#         if (length > max_length):
#             max_length=length
#             st= l+1
#             end=r-1
#
#         # for Even number
#     for i in range( n - 1):
#         r = i+1
#         l = i
#         while (l >= 0 and r < n):
#             if (s[r] == s[l]):
#                 l -= 1
#                 r += 1
#             else:
#                 break
#         lenth = r - l - 1
#         if (lenth > max_length):
#             max_length = lenth
#             st = l + 1
#             end = r - 1
#
#     return s[st:end+1]
#
# s="babad"
#
# print(LPS(s))


# 4)Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# we will use sliding window technique ,will start from 0 index and iterate through every string
# than the moment we will get repeating string ,we will increase the start point by one and get the max_length

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

#
# def lengthOfLongestSubstring(s):
#
#     if len(s)==0:
#         return 0
#     start,max_length=0,0
#     map={}
#
#     for i in range(len(s)):
#         if s[i] in map and start<=map[s[i]]:
#             start=map[s[i]]+1
#         else:
#             max_length=max(max_length,i-start+1)
#         map[s[i]]=i
#
#     return max_length
#
# result=lengthOfLongestSubstring("pwwkew")
# print(result)


# 121. Best Time to Buy and Sell Stock


# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


# def stock(prices):
#     l=0
#     r=1
#     max_profit=0
#     while(l>=0 and r<len(prices)):
#         if prices[l]<prices[r]:
#             profit= prices[r]-prices[l]
#             max_profit=max(max_profit,profit)
#         else:
#             l=r
#         r+=1
#     return max_profit
#
#
# prices= [7,1,5,3,6,4]
#
# result=stock(prices)
# print(result)


# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false


# def duplicate(nums):
#     dup=set()
#     for i in nums:
#         if i in dup:
#             return True
#         dup.add(i)
#     return False
#
# nums = [1,2,3,4]
# result=duplicate(nums)
# print(result)

# 6)
# l=[1,2,3,4,5,6,7,8,9,10]

# out=[0,2,0,4,0,6,0,8,0,10]

# new_list=[i if i%2==0 else 0 for i in range(1,11)]
# print(new_list)

# 322. Coin Change

# You are given an integer array coins representing coins of different denominations and
# an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount
# of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# def min_coin(coins,amount):
#     #   https://leetcode.com/problems/coin-change/discuss/1847630/Python-Bottom-up-DP-solution-explained
#     # this dp will hold the number of coins
#     # required for every amount from 0..amount
#     dp = [amount + 1] * (amount + 1)
#
#     # to have a sum of zero
#     # we don't need any coins i.e 0
#     dp[0] = 0
#
#     # brute force, we'll calculate
#     # the coins needed for every amount
#     # starting from 1 since we've calculated 0
#     for a in range(1, amount + 1):
#
#         # for every amount, we'll
#         # try to form coins with every
#         # available coin
#         for c in coins:
#
#             # if the current amount is less
#             # than the current coin, you can't
#             # make that amount with this coin
#             # so skip it. i.e. if a = 2 and coin = 5
#             # you should not bother computing anything here
#             if a - c >= 0:
#
#                 # otherwise, you check the min
#                 # of the num(coins) for current amount
#                 # and the 1 plus the coins required
#                 # by amount-c i.e. to make the amount 0
#                 # for e.g. if amount = 7 and coin = 3,
#                 # we can say the coins needed to make 7
#                 # would be the coin of denomination 4 (+1) and
#                 # the number of coins taken to reach 3
#                 # => 1 + dp[3] so that we can easily reach the sum i.e 7
#                 dp[a] = min(dp[a], 1 + dp[a - c])
#
#     # we need to return -1 if we weren't able to find
#     # an answer i.e. no updates were made and the amount
#     # still has the initial value we had set i.e float('inf')
#     return dp[amount] if dp[amount] != amount+1 else -1
#
#
# coins = [1, 2, 5]
# amount = 11
#
# print(min_coin(coins, amount))

#53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum
# A subarray is a contiguous part of an array.
#
# Example
#1)
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4, -1, 2, 1]
# has the largest sum = 6.
#
# def maxSubArray(nums):
#     MaxSub = nums[0]
#     cur_sum = 0
#     for n in nums:
#         if cur_sum < 0:
#             cur_sum = 0
#         cur_sum += n
#         MaxSub = max(MaxSub, cur_sum)
#     return MaxSub
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(nums))



#238. Product of Array Except Self
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# def productExceptSelf(nums):
#     output =[1] # right
#     for n in range(len(nums)-1,0,-1):
#         output.append(output[-1]*nums[n])
#     output = output[::-1]
#     left =1 
#     for n in range(len(nums)):
#         output[n] = output[n]* left
#         left *= nums[n] 
#     return output

# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.
# from typing import List
# class Solution:
#     def searchRange(self, nums:List[int], target: int) -> List[int]:
#         left =self.findleftbound(nums,target)
#         right =self.findrightbound(nums,target)
#         return [left,right]
    
    
#     def findleftbound(self, nums:List[int], target: int):
#         l,r = 0,len(nums)-1
#         index =-1

#         while l<=r:

#             mid = (l+r)//2
#             if nums[mid] == target:
#                 index = mid
#                 r = mid-1
#             elif nums[mid] < target:
#                 l = mid+1
#             else:
#                 r = mid-1
#         return index
    
#     def findrightbound(self, nums:List[int], target: int):
#             l,r = 0,len(nums)-1
#             index =-1
#             while l<=r:

#                 mid = (l+r)//2
#                 if nums[mid] == target:
#                     index = mid
#                     l = mid+1
#                 elif nums[mid] < target:
#                     l = mid+1
#                 else:
#                     r = mid-1
#             return index

# res = Solution()

# print(res.searchRange([5,7,7,8,8,10],8))

# 153. Find Minimum in Rotated Sorted Array

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# nums = [4,5,6,7,0,1,2]
# min_num = nums[0]
# for i in nums:
#     min_num = min(min_num,i)
# print(min_num)    

# def search(nums,target):
#     # print(len(nums))
#     # if (len(nums))==1:
#     #     if nums[0] == target:
#     #         return 0
#     #     return -1
#     for i in range(0,len(nums)):
#         if nums[i] == target:
#             return i
#         else:
#             return -1
        
# nums = [4,5,6,7,0,1,2]
# target = 1      

# print(search(nums,target))

# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case,
#  the max area of water (blue section) the container can contain is 49.

# def maxArea(height):
#     beg = 0
#     end = len(height)-1
#     max_area = 0
#     while beg<end:
#         max_area= max(max_area,min(height[beg],height[end])*(end-beg))
#         if height[beg]>=height[end]:
#             end-=1
#         else:
#             beg+=1
#     return max_area

# height = [1,8,6,2,5,4,8,3,7]
# %%
