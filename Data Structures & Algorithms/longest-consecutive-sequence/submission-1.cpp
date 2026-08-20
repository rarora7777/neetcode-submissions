class Solution {
public:
    int longestConsecutive(vector<int>& nums)
    {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        for (const auto& n : numSet)
        {
            if (!numSet.contains(n-1))
            {
                // start a sequence at n
                int m = n+1;
                while(numSet.contains(m))
                {
                    m++;
                }
                // sequence ended at m-1. Length = m-n
                longest = std::max(longest, m-n);
            }
        }

        return longest;
    }
};
