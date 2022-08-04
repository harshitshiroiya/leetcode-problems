# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return int(0)
        if root.left==None and root.right==None:
            return int(1)
        depth = 0
        arr = []
        def find_depth(self,node :TreeNode,depth,arr):
            if(node == None):
                return
            depth +=1
            if node.left==None and node.right==None:
                arr.append(depth)
            find_depth(self,node.left,depth,arr)
            find_depth(self,node.right,depth,arr)
            return arr
        find_depth(self,root,depth,arr)
        return max(arr)