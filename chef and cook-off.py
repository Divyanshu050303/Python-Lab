for i in range(int(input())):
    n = list(map(int, input().split()))
    m = n.count(1)
    if m == 0:
        print("Beginner")
    elif m == 1:
        print("Junior Developer")
    elif m == 2:
        print("Middle Developer")
    elif m == 3:
        print("Senior Developer")
    elif m == 4:
        print("Hacker")
    elif m == 5:
        print("Jeff Dean")
