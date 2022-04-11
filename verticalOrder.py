from collections import defaultdict
import queue
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        q = queue.Queue()
        d = defaultdict(list)
        q.put((root,0))
        while(q.qsize()>0):
            ele,index = q.get()
            d[index].append(ele.val)
            if(ele.left):
                q.put((ele.left,index-1))
            if(ele.right):
                 q.put((ele.right,index+1))
        d = dict(sorted(d.items(), key=lambda item: item[0]))
        return d.values()
