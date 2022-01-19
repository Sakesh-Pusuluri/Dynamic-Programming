class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        def helper(root):
            if root is None:
                return
            helper(root.left)
            result.append(root.val)
            helper(root.right)
        helper(root)
        return result
      
      
# Time complexity - O(N) # N will be number of elements
# Space complexity - O(N)
