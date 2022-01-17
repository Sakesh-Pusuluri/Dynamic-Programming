class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return 
        prev=None
        while(head):
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        return prev
      
          
# Time complexity - O(N)
# Space complexity - O(1)
