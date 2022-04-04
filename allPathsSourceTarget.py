class Solution:
    def allPathsSourceTarget(self, graph) :
        def dfs(node):
            path.append(node)
            if node == len(graph)-1:
                paths.append(path.copy())
                return
            for i in graph[node]:
                dfs(i)
                path.pop()
        path,paths=[],[]
        dfs(0)
        return paths
            
