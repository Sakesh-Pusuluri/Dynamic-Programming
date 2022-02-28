class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if(len(nums)==0):
            return 
        startElement,endElement = nums[0],nums[0]
        finalResult=[]
        for idx in range(1,len(nums)):
            if(endElement+1==nums[idx]):
                endElement+=1
            else:
                if(startElement == endElement):
                    finalResult.append(str(startElement))
                else:
                    finalResult.append(str(startElement)+'->'+str(endElement))
                startElement,endElement = nums[idx],nums[idx]
        if(startElement == endElement):
                finalResult.append(str(startElement))
        else:
                finalResult.append(str(startElement)+'->'+str(endElement))
        return finalResult
        
                    
        
                         
