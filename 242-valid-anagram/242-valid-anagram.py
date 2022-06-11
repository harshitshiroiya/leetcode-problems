class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) == len(t):
        #     for i in range(len(s)):
        return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')
                
        