class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
        
        if count_s == count_t:
            return True
        
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(s) == len(t):
        #     for i in range(len(s)):
        # return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')
               
        