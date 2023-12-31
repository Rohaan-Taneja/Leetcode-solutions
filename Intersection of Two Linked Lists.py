# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 ,p2 =headA ,headB
        while(p1 or p2):
            if p1==p2:
                return p1
            p1=p1.next if p1 is not None else headB
            p2=p2.next if p2 is not None else headA
        
        return 
        