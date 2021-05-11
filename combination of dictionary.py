import itertools
d ={'1': list(map(str, input().split())), '2': ['c', 'd']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))