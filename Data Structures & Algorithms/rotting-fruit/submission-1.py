class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Strategy: BFS starting from all rotten (val=2)
        # In-place mark all 1s as 2

        M, N = len(grid), len(grid[0])

        q = deque()
        num_fresh = 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    num_fresh += 1
        
        if num_fresh == 0:
            return 0
        
        def add_cell(i, j):
            nonlocal grid, M, N, q, num_fresh
            if i < 0 or j < 0 or i>=M or j>=N or grid[i][j] != 1:
                return
            
            grid[i][j] = 2
            num_fresh -= 1
            q.append((i, j))
            return
            

        dist = -1
        while q:
            dist += 1
            cur_len = len(q)
            for _ in range(cur_len):
                (i, j) = q.popleft()
                add_cell(i-1, j)
                add_cell(i, j-1)
                add_cell(i+1, j)
                add_cell(i, j+1)

        return dist if num_fresh == 0 else -1
                


        