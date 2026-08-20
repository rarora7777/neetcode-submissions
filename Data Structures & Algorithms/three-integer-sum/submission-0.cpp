class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums)
    {
        set<std::tuple<int, int, int>> triplets;
        // in-place sort: may not be ideal
        sort(nums.begin(), nums.end());

        int N = nums.size();

        for(int i=0; i<N; ++i)
        {
            int l = i+1;
            int r = N-1;
            int target = -nums[i];
            while (l < r)
            {
                if (nums[l] + nums[r] > target)
                {
                    r--;
                }
                else if (nums[l] + nums[r] < target)
                {
                    l++;
                }
                else
                {
                    triplets.insert(std::tuple<int, int, int>(nums[i], nums[l], nums[r]));
                    // std::cout<<i<<l<<r<<std::endl;
                    l++;
                    r--;
                }
            }
        }

        vector<vector<int>> out;
        out.reserve(triplets.size());
        for (const auto & tpl : triplets)
        {
            const auto [a, b, c] = tpl;
            out.push_back(vector<int>({a, b, c}));
        }
        return out;
    }
};
