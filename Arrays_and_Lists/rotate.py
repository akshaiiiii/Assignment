def rotate(list,k):
    l=list[-k:]+list[:-k]
    return l
print(rotate([1,2,3,4,5,6,7,8],3))
