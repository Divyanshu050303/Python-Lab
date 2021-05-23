n = int(input())
s = set(map(int, input().split()))
num=int(input())
for i in range(num):
    j=input().split()
    if j[0]=="remove":
        s.remove(int(j[1]))
    elif j[0]=="discard":
        s.discard(int(j[1]))
    else:
        s.pop()
print(sum(list(s)))