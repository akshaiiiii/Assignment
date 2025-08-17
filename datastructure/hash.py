class hashmap:
    def _hash(self, key):
        return hash(key) % self.size
    def __init__(self,size=10):
        self.size=size
        self.buckets=[[] for _ in range(self.size)]
    def put(self,key,value):
        index=self._hash(key)%self.size
        for i,(k,v)in enumerate (self.buckets[index]):
            if k == key:
                self.buckets[index][i]=(key,value)
                return
        self.buckets[index].append((key,value))
    def get(self,key):
        index=self._hash(key)%self.size
        for (k,v) in self.buckets[index]:
            if k==key:
                return v
        return None
    def remove(self,key):
        index=self._hash(key)%self.size
        self.buckets[index]=[(k,v) for (k,v) in self.buckets[index] if k!=key]
    def __str__(self):
        result=[]
        for i,bucket in enumerate(self.buckets):
            result.append(f"{i}:{bucket}")
        return "\n".join(result)
h=hashmap(10)
h.put("name","akshai")
print(h.get("name"))
h.put("name","ashin")
h.put("age",20)
print(h)




            
            
            

