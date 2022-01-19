class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return 
        currStack=[]
        result=[]
        while currStack or root:
            if root:
                currStack.append([root,'False'])
                root = root.left
            elif(currStack[-1][0].right and currStack[-1][1]=='False'):
                currStack[-1][1]='True'
                root = currStack[-1][0].right
            else:
                result.append(currStack[-1][0].val)
                currStack.pop()
        return result
      
      
      
# Time complexity - O(N)
# Spac complexity - O(N)
