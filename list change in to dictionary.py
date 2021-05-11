n=list(map(int, input("Enter first list").split()))
m=list(map(str, input("Enter second list").split()))
dic=dict(zip(n, m))
print(dic)