n=input("Enter the string")
alphabets=digits=special=0

for i in range(len(n)):
    if(n[i].isalpha()):
        alphabets = alphabets + 1
    elif(n[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
print("Alphabets in the string",alphabets)
print("Digit in the string",digits)
print("Special character",special)
