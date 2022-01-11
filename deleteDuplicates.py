# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        temp1=head
        temp2=head.next
        while(temp2):
            if(temp1.val==temp2.val):
                temp2=temp2.next
            else:
                temp1.next = temp2
                temp1 = temp1.next
                temp2=temp2.next
        temp1.next=None
        return head
                
        
        
        
# Time complexity - O(N)
# Space complexity - O(1)
