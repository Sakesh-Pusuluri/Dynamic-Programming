class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        result=[]
        def helper(root,level):
            if(len(result)==level):
                result.append([])
            result[level].append(root.val)
            if root.left:
                helper(root.left,level+1)
            if root.right:
                helper(root.right,level+1)
        helper(root,0)
        return result
      
# Time complexity - O(N)
# Space complexity - O(N)
