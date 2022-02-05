class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l=[]
        for node in lists:
            while(node):
                l.append(node.val)
                node=node.next
        l.sort()
        m = ListNode(0)
        s= m
        for i in l:
            newNode = ListNode(i)
            m.next = newNode
            m = m.next
        return s.next
