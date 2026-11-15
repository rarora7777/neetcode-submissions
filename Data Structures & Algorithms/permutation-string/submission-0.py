class Solution:
    def are_dicts_equal(self, d1, d2):
        for k, v in d1.items():
            if v != d2.get(k, 0):
                return False
        for k, v in d2.items():
            if v != d1.get(k, 0):
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n2 < n1:
            return False

        s1_stats = {}
        for ch in s1:
            s1_stats[ch] = s1_stats.get(ch, 0) + 1
        
        s2_stats = {}
        for i in range(n1):
            s2_stats[s2[i]] = s2_stats.get(s2[i], 0) + 1
        
        if self.are_dicts_equal(s1_stats, s2_stats):
            return True

        for i in range(n1, n2):
            old = s2[i-n1]
            new = s2[i]
            s2_stats[old] -= 1
            s2_stats[new] = s2_stats.get(new, 0) + 1
            if self.are_dicts_equal(s1_stats, s2_stats):
                return True
        
        return False
            

