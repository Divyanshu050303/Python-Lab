s=input()
c=f=0
for i in range(len(s)):
    for j in range(i):
        if s[i] == s[j]:
            f=1
            continue
        else:
            continue
    if f == 0:
        c+=1
if c == 1:
    print("IGNORE HIM!\n")
elif c % 2 == 0:
    print("CHAT WITH HER!\n")
else:
    print("IGNORE HIM!\n")
