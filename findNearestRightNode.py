import queue
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return
        q = queue.Queue()
        q.put(root)
        while(q.qsize()>0):
            _len = q.qsize()
            i=0
            while(i<_len):
                ele = q.get()
                if ele.left:
                    q.put(ele.left)
                if(ele.right):
                    q.put(ele.right)
                if(ele==u and i+1!=_len):
                    return q.get()
                elif(ele.val == u):
                     return
                i+=1
               
              
# Time complexity - O(N)

# Space complexity - O(H)
