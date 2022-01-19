class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
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
        order='False'
        for i in range(len(result)):
            if order=='True':
                result[i]=result[i][::-1]
                order='False'
            else:
                order='True'
        return result
      
      
# Time complexity - O(N)
# Space complexity - O(N)
