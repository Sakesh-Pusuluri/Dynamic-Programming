import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        result=[]
        if(len(nums)<k):
            return 
        for i in range(k):
            heapq.heappush(result,int(nums[i]))
        for i in range(k,len(nums)):
            if(result[0]<int(nums[i])):
                heapq.heappop(result)
                heapq.heappush(result,int(nums[i]))
        return str(result[0])
            
        
