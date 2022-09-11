# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode], h=1) -> bool:
        if not root: return h
        l = self.isBalanced(root.left, h+1)
        if not l: return
        r = self.isBalanced(root.right, h+1)
        if not r: return
        return abs(l-r) <= 1 and max(l, r)