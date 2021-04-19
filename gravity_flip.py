n = int(input())
b = list(map(int, input().split()))
b.sort()
for i in b:
    print(i, end=" ")