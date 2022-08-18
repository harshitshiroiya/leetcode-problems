# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptA, ptB, jumpToNext = headA, headB, False
        while ptA and ptB:
            if ptA == ptB:
                return ptA
            ptA, ptB = ptA.next, ptB.next
            if not ptA and not jumpToNext:
                ptA, jumpToNext = headB, True
            if not ptB:
                ptB = headA
        return None