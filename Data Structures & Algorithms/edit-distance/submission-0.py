class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        M = len(word1)
        N = len(word2)

        dist = {}
        
        def dfs(i, j):
            if i == M:
                return N - j
            if j == N:
                return M - i
            if (i, j) in dist:
                return dist[(i, j)]
            
            if word1[i] == word2[j]:
                dist[(i, j)] = dfs(i+1, j+1)
            else:
                res = min(min(dfs(i+1, j), dfs(i, j+1)), dfs(i+1, j+1))
                dist[(i, j)] = res + 1
            
            return dist[(i, j)]
        
        return dfs(0, 0)

        
        