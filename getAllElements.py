class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result1=[]
        result2=[]
        def helper(root,result):
            if root is None:
                return 
            helper(root.left,result)
            result.append(root.val)
            helper(root.right,result)
        helper(root1,result1)
        helper(root2,result2)
        l1=len(result1)
        result1=result1+result2
        result1.sort()
        return result1
      
      
