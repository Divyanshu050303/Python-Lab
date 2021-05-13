import heapq as hq
n=list(map(int, input("Enter the element").split()))
m=hq.nsmallest(len(n), n)
print("Original list", n)
print("After heapify", m)