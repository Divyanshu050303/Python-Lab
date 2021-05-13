import heapq as hp
n=list(map(int, input().split()))
h=[]
print("original list", n)
for i in n:
    hp.heappush(h, i)
print([hp.heappop(h) for j in range(len(h))])