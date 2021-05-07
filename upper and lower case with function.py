def upp_low(n):
    c=d=0
    for i in n:
        if i.isupper():
            c+=1
        elif i.islower():
            d+=1
        else:
            pass
    print("The lower in the string", d)
    print("The upper in the string", c)


upp_low('Divyanshu')