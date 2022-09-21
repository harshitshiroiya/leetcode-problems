class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,j in OrderedDict(Counter(s)).items():
            if j == 1:
                return s.index(i)
        return -1
#         count = collections.Counter(s)        
#         for idx, ch in enumerate(s):
#             if count[ch] == 1:
#                 return idx     
#         return -1