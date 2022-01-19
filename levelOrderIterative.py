import queue 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        q = queue.Queue()
        result=[]
        q.put(root)
        while(q.qsize()>0):
            count = q.qsize()
            subRow=[]
            while(count):
                ele = q.get()
                subRow.append(ele.val)
                if ele.left:
                    q.put(ele.left)
                if(ele.right):
                    q.put(ele.right)
                count-=1
            result.append(subRow)
        return result
      
      
      
# Time complexity - O(N)
# Space complexity - O(N)
