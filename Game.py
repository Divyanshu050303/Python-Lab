n = int(input())
m= []
b = []
c = 0
for i in range(n):
	x, y = map(int, input().split())
	m.append(x)
	b.append(y)
for i in range(n):
	for j in range(n):
		if m[i] == b[j]:
			c+=1
print(c)
'''4
100 42
42 100
5 42
100 5'''