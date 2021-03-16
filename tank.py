h=10
r=5
f=10
t=eval(input('Enter the Time'))
Vt=3.14*r*r*h
Vw=f*t
if Vw>Vt:
    print('Over Flow')
    print('Volume :',Vw-Vt)
elif Vw==Vt:
    print('Tank Full')
else :
    print('UnderFlow Condition')
    ht=Vw/(3.14*r*r)
    hr=h-ht
    print(f'Filled Height : {ht}\nRemaining Height : {hr}')
