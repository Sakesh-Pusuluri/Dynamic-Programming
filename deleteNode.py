class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def precedor(root):
            root = root.left
            while root.right :
                root = root.right
            return root.val
        def successor(root):
            root = root.right
            while root.left :
                root = root.left
            return root.val
        if root is None:
            return None
        if root.val<key:
            root.right = self.deleteNode(root.right,key)
        elif(root.val>key):
            root.left=self.deleteNode(root.left,key)
        else:
            if not ( root.left or  root.right):
                root = None
            elif(root.right):
                root.val = successor(root)
                root.right = self.deleteNode(root.right,root.val)
            else:
                root.val = precedor(root)
                root.left = self.deleteNode(root.left,root.val)
        return root
