for i in range(int(input())):
    n=int(input())
    h=input()
    if 'I' not in h and 'Y' in h:
        print('NOT INDIAN')
    elif 'I' in h:
        print('INDIAN')
    else:
        print('NOT SURE')