class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = {}
        result = ""
        
        for i in s:
            if not i in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        sorted_dic = sorted(hash_map, key=hash_map.get, reverse=True)
        for count in sorted_dic:
            result += count * (hash_map[count])
        return result