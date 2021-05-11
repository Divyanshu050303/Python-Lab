dic1={1: 10, 2: 20, 3: 30}
dic2={4: 10, 5: 20, 6: 30}
c=dic2.copy()
dic1.update(c)
print(dic1)