n=input("Enter the string")
counts = dict()
words = n.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
