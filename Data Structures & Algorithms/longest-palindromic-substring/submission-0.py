class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        maxsub_len = 0
        maxsub_idx = 0
        for i in range(N):
            left = i
            right = i
            sublen = -1
            sub_idx = left
            while left >= 0 and right < N:
                if s[left] != s[right]:
                    break
                sublen += 2
                sub_idx = left
                left -= 1
                right += 1
            if sublen > maxsub_len:
                maxsub_len = sublen
                maxsub_idx = sub_idx

            left = i
            right = i+1
            sublen = 0
            while left >= 0 and right < N:
                if s[left] != s[right]:
                    break
                sub_idx = left
                sublen += 2
                left -= 1
                right += 1
            if sublen > maxsub_len:
                maxsub_len = sublen
                maxsub_idx = sub_idx
        
        return s[maxsub_idx:(maxsub_idx + maxsub_len)]
