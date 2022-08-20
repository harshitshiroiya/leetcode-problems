# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        even_runner = head
        
        odd_head = head.next
        odd_runner = head.next
        
        while (odd_runner and odd_runner.next) and (even_runner and even_runner.next):
            even_runner.next = odd_runner.next
            even_runner = odd_runner.next
            
            if even_runner:
                odd_runner.next = even_runner.next
                odd_runner = even_runner.next
            else:
                odd_runner.next = None
                odd_runner = None
            
        even_runner.next = odd_head
        
        return head