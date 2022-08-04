class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in (strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
            print (d[key])
        return d.values()