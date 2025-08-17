def merge(l1,l2):
    n1=len(l1)
    n2=len(l2)
    l1.extend([0]*n2)
    i=n1-1
    j=n2-1
    k=n1+n2-1
    while(i>=0 and j>=0):
        if(l1[i]>l2[j]):
            l1[k]=l1[i]
            i-=1
        else:
            l1[k]=l2[j]
            j-=1
        k-=1
    while(j>=0):
        l1[k]=l2[j]
        j-=1
        k-=1
    return l1
print(merge([1,2,3],[4,5,6]))
