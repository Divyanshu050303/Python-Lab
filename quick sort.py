def quick_sort(array):
    if len(array)>1:
        k=array.pop()
        gtr, eq, smi=[], [k], []
        for i in array:
            if i==k:
                eq.append(i)
            elif i>k:
                gtr.append(i)
            else:
                smi.append(i)
        return quick_sort(smi)+eq+quick_sort(gtr)
    else:
        return array


n=list(map(int, input().split()))
print(quick_sort(n))