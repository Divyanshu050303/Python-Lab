n=int(input("Enter the class held"))
m=int(input("Enter the class attended by you "))
b=input("Have you any medical problem between class (y or n) ")
if b=='y':
    g=int(input("Enter the number of class"))
    s=m+g
    v=(s/n)*100
    if v <= 70:
        print(v, "% Sorry You will not appear in the exam")
    else:
        print(v, "% You will appear in the exam")
if b=='n':
    v=(m/n)*100
    if v>=75:
        print(v, "You will appear in the exam")
    else:
        print(v, "You will not appear in the exam")

