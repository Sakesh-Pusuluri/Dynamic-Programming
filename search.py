# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        slow,fast=0,1
        def binarySearch(slow,fast,target):
            while(slow<=fast):
                mid = (slow+fast)//2
                if(reader.get(mid)==target):
                    return mid
                elif(reader.get(mid)<target):
                    slow=mid+1
                else:
                    fast=mid-1
            return -1
        while(reader.get(fast)<target):
            newSlow = (slow+1)
            fast= newSlow*2
            slow=newSlow
        return binarySearch(slow,fast,target)
