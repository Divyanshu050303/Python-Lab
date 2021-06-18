def drow(amt):
        N = int(input("We have 100 or 500 and 2000 note only which note do you preferred"))
        if N == 500:
            M=[500, 100]
            A = B = j =0
            for i in M:
                if i == 500:
                    j = amt % i
                    A = (amt-j) // 500
                elif i == 100:
                    B = j // 100
            print("Here is your balance", A, "500 note", B, "100 notes")
            print(" Now you remaining amount", amount-amt)
        elif N == 2000:
            M = [2000, 500, 100]
            A = B =o= j= t =0
            for i in M:
                if i == 2000:
                    j = amt % i
                    A = (amt-j) // 2000
                elif i == 500:
                    o = j % i
                    B = (j - o) // 500
                else:
                    t = o // 100
            print("Here is your balance", A, "2000 note", B, "500 notes", t, "100 notes")
            print(" Now you remaining amount", amount - amt)
        elif N==100:
            print("Here is your balance", amt // 100)
            print(" Now you remaining amount", amount - amt)
        else:
            print("Sorry your choose was wrong")
        print(name+" Thank you for using our Atm")
        print("HAVE A NICE DAY")
def deposit(amt):
    print("Here is your account balance", amount+amt)
    print("HAVE A NICE DAY")


print("    + + + +   Welcome to the ATM   + + + +")
n=input("For enter the card press c")
if n=='c':
    name=input("Enter your name")
    amount=int(input("Enter your account balance"))
    m=int(input(" For with draw press 1 or deposit press 2"))
    if m== 1:
        p=int(input("Enter the pin number"))
        a=int(input("Enter the amount"))
        drow(a)
    elif m==2:
        p=int(input("Enter the pin number"))
        a=int(input("Enter the amount"))
        deposit(a)
    else:
        print("You press some thing wrong")
else:
    print("You press something wrong")
