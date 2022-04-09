class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def DFS(i):
            if i < 0:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            DFS(i - 1)
            subset.pop()
            DFS(i - 1)
        DFS(len(nums) - 1)
        return res