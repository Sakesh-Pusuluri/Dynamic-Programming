class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def heightHelper(root):
            if root is None:
                return 0
            a = 1+heightHelper(root.left)
            b = 1+ heightHelper(root.right)
            return max(a,b)
        if(abs(heightHelper(root.left) - heightHelper(root.right))>1):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
      
      
# Time complexity - O(NlogN)
# Space complexity - O(N)
