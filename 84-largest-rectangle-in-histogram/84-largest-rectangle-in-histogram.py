class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while(stack and heights[stack[-1]] > heights[i]):
                j = stack.pop()
                ans = max(ans, (i-stack[-1]-1)*heights[j])
            stack.append(i)
        return ans