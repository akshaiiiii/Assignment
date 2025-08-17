
def create(str):
    freq=[0]*26
    for char in str:
        index=ord(char)-ord('a')
        freq[index]+=1
    return freq
def anagram(str1,str2):
    if(len(str1)==len(str2)):
        freq1=create(str1)
        freq2=create(str2)
        if(freq1==freq2):
            return True
        else:
            return False
    else:
        return False
print(anagram("listenn","silennt"))