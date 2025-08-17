#quick sort has a time complexity of nlog(n) but in the worst case the stack depth become n intead of log(n) there for the time complexity become o(n2)
def partition(arr,low,high):
    pivot=arr[high]
    j=high-1
    i=low
    while i<=j:
        while(i<=j and arr[j]>pivot):
            j-=1
        while(i<=j and arr[i]<pivot):
            i+=1
        if(i<=j):
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
            j-=1
    arr[high],arr[i]=arr[i],arr[high]
    return i
def quicksort(arr,low,high):
    if low<high:
        i=partition(arr,low,high)
        quicksort(arr,low,i-1)
        quicksort(arr,i+1,high)
arr=[3,4,6,1,8,2,9]
quicksort(arr,0,6)
print(arr)