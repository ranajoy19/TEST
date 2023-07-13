# febonacci series using recursion

# def febo(n):
#     if n==1 or n==2:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         return febo(n-1)+febo(n-2)
#
# for n in range(0,20):
#     print(n ,febo(n))

# with out recursion

# def fibo(n):
#     a=0
#     b=1
#     c=0
#     if n==1 or n==2:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         for i in range(1,n):
#             c=a+b
#             a=b
#             b=c
#         return b
#
# for n in range(1,15):
#     print(n,fibo(n))
#

# basic Python Program to find Sum of Cube of Digits of a Given Number -/armstrong number

# i = int(input("enter the number"))
# check=i
# sum=0
# while (i >0):
#     sum =sum+ (i%10)*(i%10)*(i%10)
#     i=i//10
#
# if sum == check:
#     print('number is amrstrong')
# else:
#     print('number is not amrstrong')
#


# number is palindrome or not

# i=int(input('enter the number'))
# check=i
# rev=0
# while(i>0):
#     rev=(rev*10)+(i%10)      #i =151 ;rev =0+1;1*10+5=15;15*10+1=151
#     i=i//10                 # i//10=151//10=15; 5
#
# if rev== check:
#     print(check,'is palindrme number')
# else:
#     print(check,'is not palindrome number')

# same using string slicing
# i=str(input('enter the number'))
# check=i
# i=i[-1::-1]
# if i== check:
#     print(check,'is palindrme ')
# else:
#     print(check,'is not palindrome')

# method=3
# string = 'ranajoy'
# reversed = ''
#
# for i in range(len(string)-1,-1,-1):
#     reversed = reversed+ string[i]
#
# if string == reversed:
#     print(string + ': is palindrome')
# else:
#     print(string +': is not palindrome')


# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Foo” instead of the number
# and for the multiples of five print “Bar”. For numbers which are multiples of both three
# and five print “FooBar”.
# for counter in range(1,100):
#     if (counter % 3 == 0) and (counter % 5 == 0):
#       print( 'FooBar')
#     elif (counter % 3 == 0):
#         print('foo')
#     elif (counter % 5 == 0):
#         print('bar')
#     else:
#         print(counter)


# prime number from 100 to 200
# for num in range(100,201):
#     if all(num%i!=0 for i in range(2,num)):
#         print(num )

# list sorting
# l=[11, 3, 7, 5, 2]
#
# l.sort(reverse=False)
# print(l)

# list sorting without in-built
#
# old_list= [11, 3, 7, 5, 2]
# new_list= []
#
# while old_list:
#     minimum = old_list[0]
#     for x in old_list:
#         if x > minimum:
#             minimum = x
#     new_list.append(minimum)
#     old_list.remove(minimum)
# print(new_list)

# decimal to binary using recursion

# def binary(n):
#     if n==0:
#         return
#     else:
#         binary(int(n/2))
#         print(n%2 , end='')

# binary to decimal


# def decimal(n):
#     sum=0
#     i=0
#     while (n>0):               #n=1001
#         rem= n%10
#         sum = sum+ rem*pow(2,i)
#         n=int(n/10)
#         i+=1
#     return sum
#
# print(decimal(1101))

#
# num =int(input("enter the number"))
# for i in range(2,num):
#     if num%i == 0:
#         print('number is not prime')
#         break
# else:
#     print ('number is prime')
#


# for num in range(100,200):
#         if all( num%i !=0 for i in range(2,num)):
#             print(num)


# from datetime import date,datetime
# try:
#     today =datetime.today()
#     rule_date = date.today()
#     # date = date(2023, 1, 32)
#     # rule_year_start_date = datetime.strptime(str(rule_date), "%Y-%m-%d")
#     # today_date = datetime.strptime(today, "%Y-%m-%d")
#     year = rule_date.strftime("%Y")
#     month =today.strftime("%m")
#     day = today.strftime("%d")
#     final_date = datetime(int(year),int(month),int(day))
#     print(final_date,today)

# except BaseException as err:
#     print(err)