def cycle(array):
    writes=0
    for cyclestart in range(0, len(array)-1):
        item=array[cyclestart]
        pos=cyclestart
        for i in range(cyclestart+1, len(array)):
            if array[i]<item:
                pos+=1
        if pos==cyclestart:
            continue
        while item==array[pos]:
            pos+=1
        array[pos], item=item, array[pos]
        writes+=1
        while pos!=cyclestart:
            pos=cyclestart
            for i in range(cyclestart+1, len(array)):
                if array[i]<item:
                    pos+=1
            while item==array[pos]:
                pos+=1
            array[pos], item=item, array[pos]
    return writes


arr=[1, 8, 3, 9, 10, 10, 2, 4]
n=len(arr)
cycle(arr)
for i in range(0, n):
    print(arr[i], end=' ')