Height=int(input("enter the height:"))
width=int(input("enter the width:"))
max_allowed_dimension = 1000

if Height > (max_allowed_dimension):
    Height=max_allowed_dimension
    width=Height/2
    print("height =", Height)
    print("width =", width)
elif width > (max_allowed_dimension):
    width=max_allowed_dimension
    Height=width/2
    print("height =", Height)
    print("width =", width)

else:
    print("height =",Height)
    print("width = :",width)