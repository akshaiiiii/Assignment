def rotate(list,k):
    n=len(list)
    l1=[]
    for i in range(n-k,n):
        l1.append(list[i])
    for i  in range(0,n-k):
        l1.append(list[i])
    return l1
print(rotate([1,2,3,4,5,6,7,8],3))

        