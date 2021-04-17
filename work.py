n=int(input("Enter your age"))
if (n>20 and n<60):
    m=input("Enter you sex ( M or F )")
    a=input("Enter your Martial status (y or n)")
    if m=='F':
        print('you work only in urban area')
    elif m=='M' and (n<=40 and n>=20):
        print("you work anywhere")
    else:
        print("you work only in urban area")
else:
    print("ERROR")