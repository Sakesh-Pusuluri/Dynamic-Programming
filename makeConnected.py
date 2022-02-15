class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self,size):
                self.root=[i for i in range(size)]
                self.rank=[1]*size
                self.count=0
            def find(self,x):
                if(x==self.root[x]):
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]
            def union(self,x,y):
                rootX = self.find(x)
                rootY = self.find(y)
                if(rootX!=rootY):
                    if(self.rank[rootX]>self.rank[rootY]):
                        self.root[rootY] = rootX
                    elif(self.rank[rootX]<self.rank[rootY]):
                        self.root[rootX] = rootY
                    else:
                        self.root[rootY] = rootX
                        self.rank[rootX]+=1
                else:
                    self.count+=1
        uf = UnionFind(n)
        for i,j in connections:
            uf.union(i,j)
        islands=[uf.find(i) for i in uf.root]
        if(len(set(islands))-1<=uf.count):
            return len(set(islands))-1
        return -1
        
