class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        exists = set()
        left = 0
        right = 0

        max_len = right - left + 1
        exists.add(s[0])

        while (right < len(s) - 1):
            right += 1
            if s[right] in exists:
                # repeated character
                while s[left] != s[right]:
                    exists.remove(s[left])
                    left += 1
                left += 1
            else:
                exists.add(s[right])
                max_len = max(max_len, right - left + 1)
            # print(f'{left} {right}')

        return max_len