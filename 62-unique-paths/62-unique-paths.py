class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)
        
        
        #         if m == 1 or n == 1:
#             return 1
        
#         return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        
        
        
        # row = [1] * n
        # for i in range(m - 1):
        #     newRow = [1] * n
        #     for j in range(n - 2, -1, -1):
        #         newRow[j] = newRow[j + 1] + row[j]
        #     row = newRow
        # return row[0]