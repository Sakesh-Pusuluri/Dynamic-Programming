class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def helper(root):
            if root is None:
                return 
            result.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return result
      
      
# Time complexity - O(N)
# Space complexity - O(N)
