class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        hash_map = {}
        for i,n in enumerate(nums):
            x = target - n
            if x not in hash_map:
                hash_map[n] = i
            else:
                return [hash_map[x],i]
        