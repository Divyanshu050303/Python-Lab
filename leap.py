y=int(input("Enter the year"))
if y%4==0 :
    print("Leap year")
elif  y%100==0:
    print("Leap year")
elif y%400==0:
    print("Leap year")
else:
    print("Not leap year")
