class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        std::set<int> numSet(nums.begin(), nums.end());

        for (int i=0; i<nums.size(); ++i)
        {
            if (numSet.contains(target - nums[i]))
            {
                for (int j=i+1; j<nums.size(); ++j)
                {
                    if (nums[j] == target - nums[i])
                    {
                        return vector<int>({i, j});
                    }
                }
            }
        }

        return vector<int>({-1, -1});
    }
};
