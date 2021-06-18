def candy(rs):
    if n% 5==0:
        print("Here is your item")
        for i in range(rs):
            print("candy")
        print("BILL....")

        print("Thank you " + name + " for shopping")
    else:
        print("Your amount is not sufficient for candy sorry....")
def cold_drink(rs):
    if n% 20==0:
        print("Here is your item")
        for i in range(rs):
            print("cold_drink")
        print("BILL....")
        print("Thank you "+name+"for shopping")
    else:
        print("Your amount is not sufficient for cold drink sorry....")
def chocolate(rs):
    if n % 10 == 0:
        print("Here is your item")
        for i in range(rs):
            print("chocolate")
        print("BILL....")
        print("Thank you " + name + "for shopping")
    else:
        print("Your amount is not sufficient for chocolate sorry....")
def chips(rs):
    if n% 15==0:
        print("Here is your item")
        for i in range(rs):
            print("chips")
        print("BILL....")
        print("Thank you " + name + "for shopping")
    else:
        print("Your amount is not sufficient for chips sorry....")


print("= + = +  WELCOME TO THE MACHINE  = + = +")
n=int(input("Enter the rupees"))
name=input("Enter your name")
print(" 5 rupees for candy 20 rupees for cold drink 10 for chocolate 15 for chips")
m=int(input("Enter your chose 1 for candy 2 for cold drink 3 for chocolate 4 for chips"))
if m==1:
    k=int(input("How many candy do you want"))
    candy(k)
elif m==2:
    k=int(input("How many candy do you want"))
    cold_drink(k)
elif m==3:
    k=int(input("How many candy do you want"))
    chocolate(k)
elif m==4:
    k=int(input("How many candy do you want"))
    chips(k)
else:
    print("your press something wrong ..... ")