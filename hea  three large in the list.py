import heapq
n=list(map(int, input().split()))
m=heapq.nlargest(3, n)
print("The original list", n)
print("Three largest in the list", m)