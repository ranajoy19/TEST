from math import pi


def circle_area(r):
    if type(r) not in [int,float]:
        raise TypeError("the radius has to be real number")
    if r<0:
        raise ValueError("radius can't be negative")
    return pi*(r**2)



# print(circle_area(2))
# print(circle_area(0))
# print(circle_area(-3))
# print(circle_area(True))
# print(circle_area(3+5j))
# print(circle_area("radius"))