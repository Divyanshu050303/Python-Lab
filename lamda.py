from functools import reduce

num=[1, 2, 3, 4, 5, 6, 8]
f=list(filter(lambda n: n % 2==0, num))
m=list(map(lambda n: n*2, f))
print(m)

su=reduce(lambda a, b : a+b, m)
print(su)
