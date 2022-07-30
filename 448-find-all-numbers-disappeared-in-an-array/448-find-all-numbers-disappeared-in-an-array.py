class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lenn = len(nums)
        for i in range(lenn):
            val = abs(nums[i]) - 1
            nums[val] = abs(nums[val]) * -1
        res = []
        for i in range(lenn):
            if nums[i] > 0:
                res.append(i+1)
        return res
        
        
        # for n in nums:
        #     a = abs(n) - 1
        #     if nums[a] > 0: nums[a] *= -1
        # return [i+1 for i in range(len(nums)) if nums[i] > 0]