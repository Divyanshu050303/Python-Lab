n=input().split()
l=[]
for j in range(int(n[1])):
    m=list(map(float, input().split()))
    l.append(m)
s=0
for i in zip(*l):
    print( sum(i)/len(i) )