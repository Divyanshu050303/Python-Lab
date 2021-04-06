n=input("Enter the string")
v=0
c=0
for i in n:
    if(i=='a' or i=='e' or i=='o' or i=='i' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        v+=1
    else:
        c+=1
print("number of vowel in the string",v)
print("Number of consonant in the string including the space",c)
       
