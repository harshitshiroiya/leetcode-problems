class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key
