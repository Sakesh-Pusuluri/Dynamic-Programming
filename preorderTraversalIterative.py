class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        result=[]
        currStack=[]
        while currStack or root:
            if root :
                result.append(root.val)
                currStack.append(root)
                root = root.left
            else:
                ele = currStack.pop()
                root = ele.right
        return result
      
      
      
# Time complexity - O(N)
# Space complexi ty - O(N)
