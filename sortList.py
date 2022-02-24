# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        l=[]
        while(head):
            l.append(head.val)
            head = head.next
        l.sort()
        head1= ListNode(0)
        temp=head1
        for i in range(len(l)):
            temp.next = ListNode(l[i])
            temp = temp.next
        return head1.next
            
            
