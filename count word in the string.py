import collections
n=input("Enter the string")
d=collections.defaultdict(int)
for i in n:
    d[i]+=1

for i in sorted(d, key=d.get, reverse=True):
    if d[i]>1:
        print('%s %d' % (i, d[i]))
