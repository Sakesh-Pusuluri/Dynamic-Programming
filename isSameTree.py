class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(r1,r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None or r2 is None:
                return False
            if(r1.val==r2.val):
                a=helper(r1.left,r2.left)
                b= helper(r1.right,r2.right)
                return a and b
            else:
                return False
        return helper(p,q)
        
        
# Time complexity - O(N)
# Space complexity - O(N)
