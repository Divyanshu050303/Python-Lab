for i in range(int(input())):
    n=input().split()
    if int(n[0])>50 and float(n[1])<0.7 and int(n[2])>5600:
        print('10')
    elif int(n[0])>50 and float(n[1])<0.7:
        print('9')
    elif float(n[1])<0.7 and int(n[2])>5600:
        print('8')
    elif int(n[0])>50 and int(n[2])>5600:
        print('7')
    elif int(n[0])>50 or float(n[1])<0.7 or int(n[2])>5600:
        print('6')
    else:
        print('5')