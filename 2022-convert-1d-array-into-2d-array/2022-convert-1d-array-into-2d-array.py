class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []

        if len(original)==m*n:
            for row in range(m):
                result.append(original[n*row:n*row+n])

        return result