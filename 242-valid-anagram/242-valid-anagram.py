class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
        
        if count_s == count_t:
            return True
        
        return False
    
    
    
    
    
#         dict_s = {}
#         dict_t = {}
#         for i in s:
#             if not i in dict_s:
#                 dict_s[i] = 1
#             else:
#                 dict_s[i] += 1
#         print(dict_s)
        
#         for i in t:
#             if not i in dict_t:
#                 dict_t[i] = 1
#             else:
#                 dict_t[i] += 1
#         print(dict_t)
#         if dict_s == dict_t:
#             return True
#         else:
#             return False
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(s) == len(t):
        #     for i in range(len(s)):
        # return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')
               
        