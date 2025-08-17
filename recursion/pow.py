def power(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    elif n<0:
        return 1/power(x,-n)
    else:
        return x*power(x,n-1)
print(power(2,3))