class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        matrix = [[] for i in range(m)]
        curr = 0
        
        for i in range(m):
            for j in range(n):
                matrix[i].append(original[curr])
                curr += 1
                
        return matrix
#         result = []

#         if len(original)==m*n:
#             for row in range(m):
#                 result.append(original[n*row:n*row+n])

#         return result