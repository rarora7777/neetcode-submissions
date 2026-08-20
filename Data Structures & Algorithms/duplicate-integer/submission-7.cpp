class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> numSet(nums.begin(), nums.end());

        return numSet.size() != nums.size();
    }
};