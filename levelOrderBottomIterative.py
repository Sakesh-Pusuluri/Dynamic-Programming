import queue
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return
        result=deque()
        q=queue.Queue()
        q.put(root)
        while(q.qsize()>0):
            subRow=[]
            for i in range(q.qsize()):
                ele= q.get()
                subRow.append(ele.val)
                if(ele.left):
                    q.put(ele.left)
                if(ele.right):
                    q.put(ele.right)
            result.appendleft(subRow)
        return result
      
      
# Time complexity - O(N)
# Space complexity - O(N)
