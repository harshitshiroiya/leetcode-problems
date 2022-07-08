class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # # reverse
        # l = 0
        # r = len(matrix) -1
        # while l < r:
        #     matrix[l], matrix[r] = matrix[r], matrix[l]
        #     l += 1
        #     r -= 1
        # # transpose 
        # for i in range(len(matrix)):
        #     for j in range(i):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                # save the topleft
                topLeft = matrix[top][l + i]
                
                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
