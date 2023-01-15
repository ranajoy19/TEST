   # j=0

#i=0    #5

        # 5 4

        # 5 4 3

        # 5 4 3 2

#i=4    # 5 4 3 2 1

#decorator
#
# def decorator_fun(fun):
#     def Wrapper_fun():
#         print('wrapper is working ')
#         return fun('#','ranajoy')
#     print('decorator is working')
#     return Wrapper_fun()
#
#
#
# @decorator_fun
# def show(has,name):
#     print(has)
#     print(f"The Length of string is {len(name)} ")


# ternary Operator
#
# product=20
#
# discount= '50%' if product>=21 else '10%'
# print(discount)

# lambda Function
# sum = lambda a,b: a+b
# print(sum(1,2))


#dict comprehension
#
# squre={x:x**2 for x in range(0,11) }
# print(squre)





# find the number of coin in 31 cent

# 31 : 1 quater (25) 1 dime (10) ,1 nickel (5) , 1 pennies (1):

# num_coin(31) => 3

#
# def num_coin(cents):
#
#     if cents<1:
#         return 0
#     coins = [25,10,5,1]
#     num_of_coins = 0
#     for coin in coins:
#         num_of_coins += cents//coin
#         cents = cents % coin
#         if cents == 0:
#             break
#     return  num_of_coins
#
#
# print(num_coin(33))



# from datetime import datetime

# today = datetime.now()
# print (today.month)

# import datetime


# month = '12th'
# split_month = month[:-2]
# final_month = int(split_month)-1
# print(final_month)
# day = '1'
# day= int(day)
# # date = datetime.date(2019,final_month,day)
# # print(date)
# year ="2021-04-01"
# datem = datetime.datetime.strptime(year, "%Y-%m-%d" )
# date = datetime.date(datem.year,final_month,day)
# print(date)



# def check():
#         l ={"sona":2,"mona":1}

#         return l


# cond= check()
# print(cond)        

from datetime import datetime,timedelta
# from re import M

# def get_quarter(date):
#     month = date.month - 3
#     if month<=0:
#         month += 12
#     return (month - 1) // 3 + 1

# print(get_quarter(datetime.now()+timedelta(days =270)))   



# def get_month_string(date):
#     list_of_months = {1: 'JANUARY', 2: 'FEBRUARY', 3: 'MARCH',
#                       4: 'APRIL', 5: 'MAY', 6: 'JUNE', 7: 'JULY',
#                       8: 'AUGUST', 9: 'SEPTEMBER', 10: 'OCTOBER',
#                       11: 'NOVEMBER', 12: 'DECEMBER'}
#     return list_of_months[date.month]


# print(get_month_string(datetime.now()+timedelta(days =30)))    

print(datetime.today())