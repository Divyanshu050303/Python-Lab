def count(str):

    i=0
    j=0
    for x in str:
        if x.isupper():
            i+=1
        else:
            j+=1
    print(i , j)


a=input("Enter the string")
count(a)