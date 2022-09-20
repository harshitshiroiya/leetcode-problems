# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        def tree_paths(node, path, res):
            if not node:
                return res
            if not node.left and not node.right:
                res.append(path)
                return res
            
            if node.left:
                tree_paths(node.left,path+f"->{node.left.val}",res)
            if node.right:
                tree_paths(node.right,path+f"->{node.right.val}",res)
            
            return res
        
        return tree_paths(root, f"{root.val}", [])
            
        
        
        
        
        
        
#         if root is None:return 
#         paths = []
        
#         if root.left is not None:
#             paths += [f"{root.val}->{i}" for i in self.binaryTreePaths(root.left)]
        
#         if root.right is not None:
#             paths += [f"{root.val}->{i}" for i in self.binaryTreePaths(root.right)]
    
        
#         return paths if paths != [] else [str(root.val)]
        