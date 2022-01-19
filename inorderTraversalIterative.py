class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        currStack=[]
        result=[]
        while root or currStack:
            if root:
                currStack.append(root)
                root = root.left
            else:
                ele = currStack.pop()
                result.append(ele.val)
                root = ele.right
        return result
      
      
      
# Time complexity - O(N)
# Space complexity - O(N)
