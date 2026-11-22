class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        def find_area(i: int, j: int) -> int:
            nonlocal grid, M, N
            area = 1
            grid[i][j] = 0
            if i > 0 and grid[i-1][j] == 1:
                area += find_area(i-1, j)
            if j > 0 and grid[i][j-1] == 1:
                area += find_area(i, j-1)
            if i < M-1 and grid[i+1][j] == 1:
                area += find_area(i+1, j)
            if j < N-1 and grid[i][j+1] == 1:
                area += find_area(i, j+1)

            return area

        max_area = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    max_area = max(max_area, find_area(i, j))
        
        return max_area