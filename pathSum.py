class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def helper(root,remainingSum,currList,result):
            if root is None:
                return
            currList.append(root.val)
            if root.left is None and root.right is None and remainingSum ==root.val:
                result.append(list(currList))
            else:
                helper(root.left,remainingSum - root.val,currList,result)
                helper(root.right,remainingSum - root.val,currList,result)
            currList.pop()
        helper(root,targetSum,[],result)
        return result
