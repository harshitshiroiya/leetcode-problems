# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = [root]
        ret = []
        if not root:
            return []
        
        while level:
            level_sum = 0
            level_len = len(level)
            len_l = level_len
            
            while len_l:
                node = level.pop(0)
                level_sum += node.val
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                len_l -= 1
            ret.append(level_sum/level_len)
        return ret
                
        