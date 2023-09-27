# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode(0)
        cur=dummy
        c=0
        p1, p2 = l1, l2
        while(p1 or p2):
            v =(p1.val if p1 else 0) + (p2.val if p2 else 0)+ c
            c=v//10
            cur.next=ListNode(v%10)
            cur=cur.next
            p1=p1.next if p1 else None
            p2=p2.next if p2 else None
        
        if c==1:
            cur.next=ListNode(1)
        
        return dummy.next

