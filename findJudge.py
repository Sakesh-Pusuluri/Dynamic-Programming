class Solution:
    def findJudge(self, n, trust):
        graph=[0]*(n+1)
        for i,j in trust:
            graph[i]-=1
            graph[j]+=1
        for i in range(1,n+1):
            if(graph[i]==n-1):
                return i
        return -1
