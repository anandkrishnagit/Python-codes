try:
    a=int(input("enter a:"))
    b=int(input("Enter b:"))
    c=a/b
    print("a/b = %d"%c)
except Exception as c:
    print("can't divide by zero")
    print(c)
else:
    print("Hi I am else block")