n=int(input("Enter the number of subject"))
sum=0
for i in range(n):
    m=int(input("Enter the marks"))
    sum=sum+m
avg=sum/n
print(avg)
if avg<25:
    print("You got F grade try to improve a lot")
elif avg>=25 and avg<=45:
    print("You got E grade try to improve")
elif avg>=45 and avg<=50:
    print("You got D grade try to improve")
elif avg>=50 and avg<=60:
    print("You got C grade not bad but improve")
elif avg>=60 and avg<=80:
    print("You got B grade GOOD")
elif avg>80:
    print("You got A grade VERY GOOD")
else:
    print("FAIl try to next time")