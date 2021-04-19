n=input()
for i in range(0, len(n)):
    count = 1
    for j in range(i+1, len(n)):
        if n[i] == n[j] and n[i] != ' ':
            count = count + 1
            string = n[:j] + '0' + n[j+1:]
    if count > 1 and n[i] != '0':
        print(len(n[i]),len(n))
print(n)