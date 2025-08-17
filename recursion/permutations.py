def perm(s,l,r):
    if l==r:
        print(''.join(s))
    else:
        for i in range(l,r+1):
            s[i],s[l]=s[l],s[i]
            perm(s,l+1,r)
            s[i],s[l]=s[l],s[i]
perm(list('abc'),0,2)
