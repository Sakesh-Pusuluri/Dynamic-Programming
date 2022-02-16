# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if temp is None or temp.next is None:
            return temp
        if temp and temp.next:
            temp1 = temp
            temp2 = temp.next
            temp3 = temp2.next
            temp = temp2
            temp2.next = temp1
            temp1.next = temp3
        temp.next.next = self.swapPairs(temp.next.next)
        return temp
        
