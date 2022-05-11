from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        result=[0]*k
        logs_dict=defaultdict(set)
        for i,j in logs:
            logs_dict[i].add(j)
        for key,val in logs_dict.items():
            result[len(val)-1]+=1
        return result
