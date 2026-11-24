class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        l = 0
        r = M * N - 1

        while l <= r:
            # print(l, r)
            mid = l + ((r-l) // 2)
            i, j = mid // N, mid % N
            # print(mid, i, j, matrix[i][j])
            if target > matrix[i][j]:
                l = mid + 1
            elif target < matrix[i][j]:
                r = mid - 1
            else:
                return True
        
        return False