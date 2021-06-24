k=int(input())
n=list(map(int, input().split()))
not_ready=ready=0
for i in range(k):
    if n[i]% 2==0:
        ready+=1
    else:
        not_ready+=1
if ready>not_ready:
    print("READY FOR BATTLE")
else:
    print("NOT READY")