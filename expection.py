try:
    a=int(input("enter A"))
    b=int(input("enter B"))
    c=a/b
    print("a/b=%d"%c)
except:
    print("can't divide by zero")
    print(Exception)
else:
    print("Hi I am else block")