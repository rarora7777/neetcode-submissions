class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        exists = {}
        left = 0
        right = 0

        max_len = right - left + 1
        exists[s[0]] = True

        while (right < len(s) - 1):
            right += 1
            if exists.get(s[right], False):
                # repeated character
                while s[left] != s[right]:
                    exists[s[left]] = False
                    left += 1
                left += 1
            else:
                exists[s[right]] = True
                max_len = max(max_len, right - left + 1)
            # print(f'{left} {right}')

        return max_len