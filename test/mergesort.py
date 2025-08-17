#time complexity is nlog(n),it is a stable sorting and also its is not an inplace algorithm
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr,left,right)
def merge(arr,l,r):
    i=j=k=0
    while(i<len(l) and j<len(r)):
        if(l[i]<=r[j]):
            arr[k]=l[i]
            k+=1
            i+=1
        else:
            arr[k]=r[j]
            k+=1
            j+=1
    while(i<len(l)):
        arr[k]=l[i]
        k+=1
        i+=1
    while(j<len(r)):
        arr[k]=r[j]
        k+=1
        j+=1
arr=[4,1,2,3,7,8]
merge_sort(arr)
print(arr)

