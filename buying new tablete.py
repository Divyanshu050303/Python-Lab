for i in range(int(input())):
    n, b=map(int, input().split())
    max_area=0
    for j in range(n):
        w, h, p=map(int, input().split())
        if b>=p:
            area=h*w
            if area>max_area:
                max_area=area
    if max_area==0:
        print("no tablet")
    else:
        print(max_area)