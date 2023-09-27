# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        p=head
        c=0
        while(p.next):
            p=p.next
            c +=1
            if c >=n:
                cur=cur.next
        agla=cur.next.next
        cur.next=agla
        return dummy.next
        