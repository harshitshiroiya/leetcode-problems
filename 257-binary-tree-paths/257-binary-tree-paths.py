# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        A, P = [], []
        def dfs(N):
            if N == None: return
            P.append(N.val)
            if (N.left,N.right) == (None,None): A.append('->'.join(map(str,P)))
            else: dfs(N.left), dfs(N.right)
            P.pop()
        dfs(root)
        return A