# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1, h2 = None, None
        n      = head
        while n:
            if n.val<x:
                if h1:
                    n1.next = n
                else:
                    h1      = n
                n1 = n
            else:
                if h2:
                    n2.next = n
                else:
                    h2      = n
                n2 = n
            n = n.next
        if h1:
            n1.next = h2
        if h2:
            n2.next = None
        return h1 or h2