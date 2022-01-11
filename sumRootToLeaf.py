# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.s=''
        self._sum=0
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.s+=str(root.val)
        if root.left is None and root.right is None:
            self._sum+=int(self.s,2)
        self.sumRootToLeaf(root.left)
        self.sumRootToLeaf(root.right)
        self.s=self.s[:-1]
        return self._sum
