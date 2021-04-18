def fig(n):
    if n>0:
        a=0
        b=1
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2, n):
                c=a+b
                a=b
                b=c
                print(c)
    else:
        print("You entered invalid number")

m=int(input("Enter the number you want in fibonacci"))
fig(m)
