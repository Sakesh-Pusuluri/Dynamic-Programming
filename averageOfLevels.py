import queue
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        q=queue.Queue()
        q.put(root)
        while(q.qsize()>0):
            _sum=0
            eleLen = q.qsize()
            for _ in range(eleLen):
                ele = q.get()
                if ele.left:
                    q.put(ele.left)
                if ele.right:
                    q.put(ele.right)
                _sum+=ele.val
            result.append(_sum/(eleLen))
        return result
      
      
      
# Time complexity - O(N)
# Space complexity - O(H)
