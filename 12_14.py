table_12=[]
for i in range(1,121):
    if i % 12==0:
        table_12.append(i)
print(table_12)
table_14=[]
for i in table_12:
    i=i+2    
    table_14.append(i)

print(table_14)