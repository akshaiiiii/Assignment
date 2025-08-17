def binary(list,k):
    l=0
    r=len(list)-1
    while(l<=r):
        mid=(l+r)//2
        if(list[mid]>k):
            r=mid-1
        elif(list[mid]<k):
            l=mid+1
        else:
            return mid
    return -1
print(binary([1,2,3,4],8))
        

