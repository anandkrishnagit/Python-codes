try:
    a=10/0
except(ArithmeticError,IOError):
    print("Arithmatic Exception")
else:
    print("successfully done")