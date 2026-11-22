class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])

        conn_idx = 0

        def mark_conn_comp(i, j):
            nonlocal grid, M, N
            grid[i][j] = ""
            if i > 0 and grid[i-1][j] == "1":
                mark_conn_comp(i-1, j)
            if j > 0 and grid[i][j-1] == "1":
                mark_conn_comp(i, j-1)
            if i < M-1 and grid[i+1][j] == "1":
                mark_conn_comp(i+1, j)
            if j < N-1 and grid[i][j+1] == "1":
                mark_conn_comp(i, j+1)

        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    mark_conn_comp(i, j)
                    conn_idx += 1
        
        return conn_idx