class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        dictionary={}
        for i in nums1:
            for j in nums2:
                dictionary[i+j] = dictionary.get(i+j,0)+1
        output=0
        for k in nums3:
            for l in nums4:
                output += dictionary.get(-(k+l),0)
        return output
      
      
# Time complexity -  O(N^2)
# Space complexity - O(N^2)
                
