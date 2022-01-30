# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.ans=1
        def height(root):
            if root is None:
                return 0
            a = height(root.left)
            b = height(root.right)
            self.ans=max(self.ans,a+b+1)
            return 1+max(a,b)
        height(root)
        return self.ans-1
