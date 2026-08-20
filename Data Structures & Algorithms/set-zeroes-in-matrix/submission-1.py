class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        if M == 0:
            return
        
        N = len(matrix[0])

        zeroRow = [False] * M
        zeroCol = [False] * N

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    zeroRow[i] = True
                    zeroCol[j] = True
        

        for i in range(M):
            for j in range(N):
                if zeroRow[i] or zeroCol[j]:
                    matrix[i][j] = 0
        