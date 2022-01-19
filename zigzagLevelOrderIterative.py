import queue
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        q = queue.Queue()
        result=[]
        order='False'
        q.put(root)
        while(q.qsize()>0):
            count = q.qsize()
            if order=='True':
                order = 'False'
            else:
                order='True'
            subRow=[]
            while(count):
                ele = q.get()
                subRow.append(ele.val)
                if(ele.left):
                    q.put(ele.left)
                if(ele.right):
                    q.put(ele.right)
                count-=1
            if order=='False':
                result.append(subRow[::-1])
            else:
                result.append(subRow)
        return result
      
      
# Time complexity - O(N)
# Space complexity - O(N)
