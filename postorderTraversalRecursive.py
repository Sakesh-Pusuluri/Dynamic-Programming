class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        def helper(root):
            if root is None:
                return 
            helper(root.left)
            helper(root.right)
            result.append(root.val)
        helper(root)
        return result
      
      
# Time complexity - O(N)
# Space complexity - O(N)
