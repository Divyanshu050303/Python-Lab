a=input()
length_cond=(8<=len(a)<=32)
Start_cond=(a[0].isalpha())
special_ch=("/" not in a ) and ("\\" not in a) and ("=" not in a) and ("'" not in a) and ('"' not in a)
spaces_cond= " " not in a 
print(length_cond and Start_cond and special_ch and spaces_cond)
