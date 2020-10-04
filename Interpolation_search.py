def inter(arr,key):
    l=len(arr)
    lo=0
    hi=l-1
    vlo=arr[lo]
    vhi=arr[hi]
    while (lo<=hi and (key>arr[lo] and key<arr[hi])):
        if lo==hi:
            if arr[lo]==key:
                return lo
            else:
                return -1
        pos = int(lo + ((key - arr[lo]) / (arr[hi] - arr[lo])) * (hi - lo))
        if arr[pos]==key:
            return pos
        elif arr[pos]>key:
            hi=pos-1
        elif arr[pos]<key:
            lo=pos+1
    return -1



arr=[1,3,5,7,9,11,13,15,17]
key=15
print(inter(arr,key))