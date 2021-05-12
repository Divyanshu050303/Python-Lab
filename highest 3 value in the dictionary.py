from heapq import nlargest
n=int(input("Enter the length of dictionary"))
dic={}
for i in range(n):
    key=input("Enter the key first")
    value=input("Enter the value ")
    dic[key]=value
print("The original list:", dic)
three_largest=nlargest(3, dic, key=dic.get)
print("three large value in the dictionary", three_largest)
#'a':500, 'b':5874, 'c': 560,'d':400,