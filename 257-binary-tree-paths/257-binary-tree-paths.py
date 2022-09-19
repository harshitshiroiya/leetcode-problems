# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:return 
        paths = []
        
        if root.left is not None:
            paths += [f"{root.val}->{i}" for i in self.binaryTreePaths(root.left)]
        
        if root.right is not None:
            paths += [f"{root.val}->{i}" for i in self.binaryTreePaths(root.right)]
    
        
        return paths if paths != [] else [str(root.val)]
        