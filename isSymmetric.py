class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 
        def helper(r1,r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None or r2 is None:
                return False
            if(r1.val == r2.val):
                a = helper(r1.left,r2.right)
                b = helper(r1.right,r2.left)
                return a and b
            else:
                return False
        return helper(root.left,root.right)
      
      
# Time complexity - O(N)
# Space complexity - O(N)
