class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  
                return False
        return len(stack) == 0
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack, match = [], {')': '(', ']': '[', '}': '{'}
        # for ch in s:
        #     if ch in match:
        #         if not (stack and stack.pop() == match[ch]):
        #             return False
        #     else:
        #         stack.append(ch)
        # return not stack