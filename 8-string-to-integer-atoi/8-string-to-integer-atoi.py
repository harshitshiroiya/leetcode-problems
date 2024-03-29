MAPPING = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}

MAX_INT = 2**31-1
MIN_INT = -(2**31)

class Solution:
    def myAtoi(self, s: str) -> int:
        ls = s.strip(' ')
        if not ls:
            return 0
        
        sign = -1 if ls[0] == "-" else 1
        if sign != 1 or ls[0] == "+":
            ls = ls[1:]
            
        res = 0
        for c in ls:
            if c not in MAPPING:
                return self.limit(res * sign)
            
            res *= 10
            res += MAPPING[c]
            
        return self.limit(res * sign)
    
    def limit(self, x: int) -> int:
        if x > MAX_INT:
            return MAX_INT
        if x < MIN_INT:
            return MIN_INT
        return x