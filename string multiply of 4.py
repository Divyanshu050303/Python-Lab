n=input("Enter the string")
if len(n)% 4==0:
    print(''.join(reversed(n)))
else:
    print(n)