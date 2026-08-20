class Solution {
public:
    int longestConsecutive(vector<int>& nums)
    {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        // let |nums| = N
        // Since the condition CN only passes at the start of a continuous sequence,
        // condition CM is checked at most once for each element:
        // zero times for the first element of any cont. seq.
        // once for every other element of any cont. seq.
        // Thus, # of times the inner loop runs overall < N, therefore that computation is O(N)
        for (const auto& n : numSet)
        {
            // this condition ensures that we only run the while loop for actual
            // LCS starts, and not in the middle of a LCS
            if (!numSet.contains(n-1))      //  CN
            {
                // start a sequence at n
                int m = n+1;
                while(numSet.contains(m))   //  CM
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
