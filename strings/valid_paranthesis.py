def valid_para(str):
    stk=[]
    hashmap={")":"(","}":"{","]":"["}
    for char in str:
        if char  in hashmap.values():
            stk.append(char)
        elif char  in hashmap:
            if stk[-1]!=hashmap[char] or not stk:
                return False
            else:
                stk.pop()
        else:
            continue
    return len(stk)==0
        
print(valid_para("{(([]))}"))