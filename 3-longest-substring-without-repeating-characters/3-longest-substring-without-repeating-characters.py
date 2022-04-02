class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        l = {}
        ans = 0
        
        while j < len(s):
            if s[j] not in l or i>l[s[j]]:
                ans = max(ans,(j-i+1))
                l[s[j]] = j
            else:
                i = l[s[j]]+1
                ans = max(ans,(j-i+1))
                j-=1
         
            j+=1
        return ans    