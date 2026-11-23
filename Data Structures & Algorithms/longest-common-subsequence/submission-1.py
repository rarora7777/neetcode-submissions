class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M = len(text1)
        N = len(text2)

        lcs = [[0] * (N+1) for _ in range(M+1)]

        for i in range(M):
            for j in range(N):
                if text1[i] == text2[j]:
                    lcs[i+1][j+1] = lcs[i][j] + 1
                else:
                    lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j])
        
        # for i in range(M+1):
        #     print(lcs[i])

        return lcs[M][N]
