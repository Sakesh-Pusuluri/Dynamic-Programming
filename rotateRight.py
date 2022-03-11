# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0:
            return head
        if head is None:
            return None
        if not head.next:
            return head
        def lengthLL(temp):
            count=0
            while temp:
                count+=1
                temp=temp.next
            return count
        slow,fast=head,head
        k = k%lengthLL(head)
        if k==0:
            return head
        while(k):
            fast=fast.next
            k-=1
        while(fast.next is not None):
            slow = slow.next
            fast = fast.next
        temp=slow.next
        fast.next=head
        slow.next=None
        head=temp
        return head
