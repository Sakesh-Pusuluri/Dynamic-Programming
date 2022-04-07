class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[-i for i in stones]
        heapq.heapify(maxHeap)
        while(len(maxHeap)>1):
            val1 = heapq.heappop(maxHeap)
            val2 = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -1* abs(val1-val2))
        if(len(maxHeap)==0):
            return 0
        else:
            return -1*maxHeap[0]
        
