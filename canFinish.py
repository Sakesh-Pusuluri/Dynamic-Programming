import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses= collections.defaultdict(list)
        for j,i in prerequisites:
            courses[i].append(j)
        visited=set()
        def dfs(course):
            if course in visited:
                return False
            if courses[course] ==[]:
                return True
            visited.add(course)
            for c in courses[course]:
                if not(dfs(c)):
                    return False
            visited.remove(course)
            courses[course]=[]
            return True
        for course in range(numCourses-1):
            if not(dfs(course)):
                return False
        return True
    
            
        
