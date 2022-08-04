"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        return self.helper(root)
    def helper(self, root, parent=None, isleftChild=True):
        if root is None:
            return None
        
        if parent == None:
            root.next = None
        else:
            if isleftChild:
                root.next = parent.right
            else:
                root.next = None
                if parent.next != None:
                    root.next = parent.next.left
                    
        root.left = self.helper(root.left, root, True)
        root.right = self.helper(root.right, root, False)
        
        return root
    
    
    