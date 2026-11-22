class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M = len(grid)
        N = len(grid[0])
        
        queue = deque()
        visited = set()

        def add_cell(i, j):
            if i<0 or j<0 or i==M or j==N:
                return
            if grid[i][j] == -1 or (i, j) in visited:
                return
            
            visited.add((i, j))
            queue.append((i, j))

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    add_cell(i, j)
        
        dist = 0
        while queue:
            K = len(queue)
            for _ in range(K):
                i, j = queue.popleft()
                grid[i][j] = dist
                add_cell(i-1, j)
                add_cell(i, j-1)
                add_cell(i+1, j)
                add_cell(i, j+1)
            dist += 1