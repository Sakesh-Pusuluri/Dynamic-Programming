class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n=len(nums)
        visited=set()
        for start in range(n):
            count,temp=0,''
            for ele in range(start,n):
                if(nums[ele]%p==0):
                    count+=1
                if(count>k):
                    break
                temp+=str(nums[ele])+','
                visited.add(temp)
        return len(visited)
    
    
