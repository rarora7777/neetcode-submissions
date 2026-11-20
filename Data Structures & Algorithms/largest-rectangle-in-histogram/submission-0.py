class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        barrier_left = [-1] * N
        barrier_right = [N] * N

        stack = []
        for i, h in enumerate(heights):
            while stack and stack[-1][1] >= h:
                stack.pop()
            if stack:
                barrier_left[i] = stack[-1][0]
            stack.append((i, h))
        
        stack.clear()
        for i, h in reversed(list(enumerate(heights))):
            while stack and stack[-1][1] >= h:
                stack.pop()
            if stack:
                barrier_right[i] = stack[-1][0]
            stack.append((i, h))
        
        maxArea = 0
        for i in range(N):
            maxArea = max(maxArea, heights[i] * (barrier_right[i] - barrier_left[i] - 1))
        
        return maxArea
        
            