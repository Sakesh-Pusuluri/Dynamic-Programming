class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for idx in range(len(equations)):
            graph[equations[idx][0]][equations[idx][1]] = values[idx]
            graph[equations[idx][1]][equations[idx][0]] = 1/values[idx]
        def dfs(x,y,visited):
            if(x not in graph or y not in graph):
                return -1
            elif(y in graph[x]):
                return graph[x][y]
            for i in graph[x]:
                if(i not in visited):
                    visited.add(i)
                    temp=dfs(i,y,visited)
                    if(temp==-1):
                        continue
                    else:
                        return temp*graph[x][i]
            return -1
        result=[]
        for x,y in queries:
            result.append(dfs(x,y,set()))
        return result
