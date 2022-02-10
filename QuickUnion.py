class QuickUnion:
    def __init__(self,size):
        self.root=[i for i in range(size)]
    def find(self,x):
        while(self.root[x]!=x):
            x = self.root[x]
        return x
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if(rootX!=rootY):
            self.root[rootY] = rootX
    def connected(self,x,y):
        return self.find(x)==self.find(y)
      
      
# union complexity - O(N) # we need to do find operation in union 
# find complexity - O(N)
# Space complexity - O(N)
