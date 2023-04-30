x=int(input("enter the first no"))
y=int(input("enter the second no"))
z=int(input("enter the third no"))
if ((x>=y) and (x>=z)):
    print(" largest= ",x)
elif((y>=x) and (y>=z)):
    print("largest= ",y)
elif((z>=x) and (z>=y)):
    print("largest= ",z)