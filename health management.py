def getdate():
    import datetime
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for exercise and 2 for food"))
        if c==1:
            v=input("Type here\n")
            with open("fig-ex.txt", "a")as op:
                op.write(str([str(getdate())])+":"+v+'\n')
                print("successfully written")
        elif c== 2:
            value = input("type here\n")
            with open("fid-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("successfully written")
        else:
            print('please enter valid choose')
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            v = input("Type here\n")
            with open("fid-ex.txt", "a")as op:
                op.write(str([str(getdate())]) + ":" + v + '\n')
                print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("fid-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("successfully written")
        else:
            print("Please enter valid choose ")
    elif k == 3:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            v = input("Type here\n")
            with open("zig-ex.txt", "a")as op:
                op.write(str([str(getdate())]) + ":" + v + '\n')
                print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("zig-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
                print("successfully written")
        else:
            print("please enter a valid choose ")
    else:
        print("Enter valid choose")
def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for exercise 2 for food"))
        if c==1:
            with open("fig-ex.txt") as op:
                for i in op:
                    print(i, end='')
        elif c==2:
            with open("fig-food.txt")as op:
                for i in op:
                    print(i, end="")
        else:
            print("Please entre a valid choose")
    elif k==2:
        c=int(input("Enter 1 for exercise 2 for food"))
        if c==1:
            with open("fid-ex.txt") as op:
                for i in op:
                    print(i, end='')
        elif c==2:
            with open("fid-food.txt")as op:
                for i in op:
                    print(i, end="")
        else:
            print("Please enter a valid choose ")
    elif k==3:
        c=int(input("Enter 1 for exercise 2 for food"))
        if c==1:
            with open("fig-ex.txt") as op:
                for i in op:
                    print(i, end='')
        elif c==2:
            with open("fig-food.txt")as op:
                for i in op:
                    print(i, end="")
        else:
            print("Please enter a valid choose")
    else:
        print("please enter valid choose")


print("health management system: ")
a=int(input("press 1 for lock the value and 2 for retrieve "))

if a==1:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
    take(b)
else:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)