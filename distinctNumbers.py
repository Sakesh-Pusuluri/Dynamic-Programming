class Solution:
    def distinctNumbers(self, nums, k):
        ans=[]
        numDict={}
        i,j=0,0
        while(j<len(nums)):
            numDict[nums[j]] = numDict.get(nums[j],0)+1
            j+=1
            if(j-i==k):
                ans.append(len(numDict))
                if(numDict[nums[i]]>1):
                    numDict[nums[i]]-=1
                else:
                    del numDict[nums[i]]
                i+=1
        return ans 
            
            
            
