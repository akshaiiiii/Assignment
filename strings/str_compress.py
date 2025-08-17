def str_comp(string):
    i=0
    result=[]
    while(i<len(string)):
        count=1
        curr=string[i]
        while( i+1 < len(string)and string[i]==string[i+1]):
            count+=1
            i+=1
        result.append(curr)
        result.append(str(count))
        i+=1
    comp=''.join(result)
    print(comp)        
str_comp("hello")
