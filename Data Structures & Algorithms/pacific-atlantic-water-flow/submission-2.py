class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M = len(heights)
        N = len(heights[0])

        # Top and left edges can flow into the pacific trivially
        def mark_grid(iter):
            nonlocal heights, M, N

            queue = deque()
        
            def mark_cell(i, j, min_val=0):
                nonlocal grid, heights, M, N, queue
                if i < 0 or j <0 or i >= M or j >= N or heights[i][j] < min_val or grid[i][j]==1:
                    return
                
                grid[i][j] = 1
                queue.append((i, j))
        
            grid = [[0] * N for _ in range(M)]
            min_val = 0
            
            J0 = 0 if iter == 0 else N-1
            I0 = 0 if iter == 0 else M-1

            for i in range(M):
                mark_cell(i, J0, min_val)
            for j in range(N):
                mark_cell(I0, j, min_val)

            while queue:
                i, j = queue.popleft()
                min_val = heights[i][j]
                mark_cell(i-1, j, min_val)
                mark_cell(i, j-1, min_val)
                mark_cell(i+1, j, min_val)
                mark_cell(i, j+1, min_val)
        
            return grid

        grid0 = mark_grid(0)
        for i in range(M):
            print(grid0[i])
        grid1 = mark_grid(1)
        for i in range(M):
            print(grid1[i])

        res = []
        for i in range(M):
            for j in range(N):
                if grid0[i][j] == 1 and grid1[i][j] == 1:
                    res.append([i, j])
        
        return res


        
