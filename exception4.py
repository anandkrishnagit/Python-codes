try:
    #file doesn't exist.
    fileptr = open("file.txt","r")
except IOError:
    print("File not found")
else:
    print("the file opened succesfully")
    fileptr.close()