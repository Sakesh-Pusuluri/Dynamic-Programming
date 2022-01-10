# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        def middle(head):
            slow,fast=head,head
            while(fast is not None and fast.next is not None):
                slow=slow.next
                fast=fast.next.next
            return slow

        def reverse(temp):
            prev=None
            while(temp):
                temp1=temp.next
                temp.next=prev
                prev=temp
                temp=temp1
            return prev
        middleElement = middle(head)
        middleElement.next = reverse(middleElement.next)
        ptr1=head
        ptr2=middleElement.next
        while(ptr2 is not None):
            temp=ptr1.next
            temp2=ptr2.next
            ptr1.next=ptr2
            ptr2.next=temp
            ptr1=ptr1.next.next
            ptr2=temp2
        middleElement.next=None
        
        
        
# Time complexity - O(N)
# Space complexity - O(1)
