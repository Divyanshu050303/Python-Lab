def binary_search(l, low, high, n):
    if high>low:
        mid=(high+low)//2
        if l[mid]==n:
            return mid
        elif l[mid]>n:
            return binary_search(l, low, mid-1, n)
        else:
            return binary_search(l, mid+1, high, n)
    else:
        return -1


l=list(map(int, input("Enter the list").split()))
n=int(input("Enter the number which do you want to search"))
result=binary_search(l, 0, len(l)-1, n)
if result !=-1:
    print("Element present at index", str(result))
else:
    print("Element is not present in the list")
