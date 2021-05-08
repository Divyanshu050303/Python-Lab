n=input("Enter the r for area rectangle  and  v for volume of cylinder")
if n=="r":
    l=int(input("Enter the length"))
    b=int(input("Enter the breath"))
    a=l* b
    decimals = 2
    print("The area of rectangle is:{0:.{1}f}cm\u00b2".format(a, decimals))
elif n=="v":
    r=int(input("Enter the radius of cylinder"))
    h=int(input("Enter the height of the cylinder"))
    v=3.14*r*r*h
    decimals=3
    print("The volume of the cylinder is :{0:.{1}f}cm\u00b3".format(v, decimals))
else:
    print("Invalid choose")