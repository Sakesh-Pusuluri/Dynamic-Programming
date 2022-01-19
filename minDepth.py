class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        a = 1 + self.minDepth(root.left)
        b = 1 + self.minDepth(root.right)
        if a == 1 and b==1:
            return 1
        if a==1 or b==1:
            return max(a,b)
        else:
            return min(a,b)
          
          
# Time complexity - O(N)
# Space complexity - O(N)
