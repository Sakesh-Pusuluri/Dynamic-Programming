class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        a = 1+ self.maxDepth(root.left)
        b = 1+ self.maxDepth(root.right)
        return max(a,b)
