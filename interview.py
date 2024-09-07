import time

l = [1, 2, 3, 4, 5, 6, 7, 4, 5, 3, 2]


# uniqueSet = ()
# for i in l:
#     if i not in uniqueSet:
#         uniqueSet.add(i)


# def dummy(n):
#     try:
#         for i in n:
#             try:
#                 print(5 / i)
#             except Exception as err:
#                 return("error", err)

#     except Exception as err:
#         print("error1", err)


x = [1, 2, 0, 2]
# dummy(x)


def decorator(fun):
    def wrapper(*agrs):
        t1 = time.time()
        result = fun()
        t2 = time.time()
        print("time", t2 - t1)
        return result

    return wrapper


@decorator
def test():
    time.sleep(2)
    return "completed"

test()





