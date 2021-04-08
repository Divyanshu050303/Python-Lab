n=input("Enter the string")
v=d=s=c=0
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u') or (i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        v+=1
    
    elif(i.isdigit()) :
        d+=1
    elif(i.isspace()):
        s+=1
    else:
        c+=1
 
    
 
    
print("Number of vowel",v)
print("Number of digit",d)
print("Number of space",s)
print("Number of consonants",c)
        
