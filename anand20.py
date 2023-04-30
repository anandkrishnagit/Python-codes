a=int(input("enter the start number "))
b=int(input("enter the end number"))
count=0
for i in range (a,b):
    if i>1:
        for j in range (2,i):
            if(i%j==0):
                break
            else:
                print(i)
                count= count+1
print("total prime no between{0} and{2}".format(n,m,count))