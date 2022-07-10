# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        self.res = -sys.maxsize-1
        self.oneSideSum(root)
        return self.res

# compute one side maximal sum, 
# (root+left children, or root+right children),
# root is the included top-most node 
    def oneSideSum(self, root):
        if not root:
            return 0
        l = max(0, self.oneSideSum(root.left))
        r = max(0, self.oneSideSum(root.right))
        self.res = max(self.res, l+r+root.val)
        return max(l, r)+root.val



#         res = [root.val]
        
#         def dfs(root):
#             if not root:
#                 return 0
            
#             leftMax = dfs(root.left)
#             rightMax = dfs(root.right)
#             leftMax = max(leftMax, 0)
#             rightMax = max(rightMax, 0)
            
#             # compute max path sum WITH split
#             res[0] = max(res[0], root.val + leftMax + rightMax)
#             return root.val + max(leftMax, rightMax)
        
#         dfs(root)
#         return res[0]