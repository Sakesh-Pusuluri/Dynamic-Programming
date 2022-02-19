from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(set)
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)
        return self.dfs(graph,set(),source,destination)
    def dfs(self,graph,visited,source,destination):
        if(source==destination):
            return True
        for node in graph[source]:
            if node not in visited:
                visited.add(node)
                val = self.dfs(graph,visited,node,destination)
                if val:
                    return True
        else:
            return False
          
      
