class Solution:
    def frequencySort(self, s: str) -> str:
#         hash_map = {}
        
#         for i in s:
#             if not i in hash_map:
#                 hash_map[i] = 1
#             else:
#                 hash_map[i] += 1

                
        cnt = collections.Counter(s)
        res = []
        for k, v in cnt.most_common():
            res += [k] * v
        return "".join(res)