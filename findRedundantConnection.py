class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self,size):
                self.root = [i for i in range(size)]
                self.rank = [1]*size
                
            def find(self,x):
                if(x==self.root[x]):
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]
            def union(self,x,y):
                rootX = self.find(x)
                rootY = self.find(y)
                if(rootX!=rootY):
                    if(self.rank[rootX]<self.rank[rootY]):
                        self.root[rootX] = rootY
                    elif(self.rank[rootX]>self.rank[rootY]):
                        self.root[rootY] = rootX
                    else:
                        self.root[rootY] = rootX
                        self.rank[rootX]+=1
            def isConnected(self,x,y):
                return self.find(x) == self.find(y)
            
        uf = UnionFind(len(edges))
        result=[]
        for edge in edges:
            if(uf.isConnected(edge[0]-1,edge[1]-1)):
                result.append([edge[0],edge[1]])
            else:
                uf.union(edge[0]-1,edge[1]-1)
        return result[-1]
        
