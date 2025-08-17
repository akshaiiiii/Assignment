def add(m1,m2):
    result=[]
    for i in range(len(m1)):
        row=[]
        for j in range(len(m1[0])):
            row.append(m1[i][j]+m2[i][j])
        result.append(row)
    return result
def multiply(m1,m2):
    result=[]
    for i in range(len(m1)):
        row=[]
        for j in range(len(m2)):
            val=0
            for k in range(len(m2[0])):
                val+=m1[i][k]*m2[k][j]
            row.append(val)
        result.append(row)
    return result
def transpose(m1):
    result=[]
    for i in range(len(m1)):
        row=[]
        for j in range(len(m1[0])):
            row.append(m1[j][i])
        result.append(row)
    return result
m1=[[1,2,3],[4,5,6],[1,2,3]]
m2=[[1,2,3],[4,5,6],[1,2,3]]
print(add(m1,m2))
print(multiply(m1,m2))
print(transpose(m1))