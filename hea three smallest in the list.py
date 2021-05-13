import heapq
n=list(map(int, input().split()))
m=heapq.nsmallest(3, n)
print("The original list", n)
print("Three smallest element", m)