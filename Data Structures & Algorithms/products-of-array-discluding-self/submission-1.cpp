class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums)
    {
        bool nonZeroFound = false;
        int nzProd = 1;
        int zeroIdx = -1;
        vector<int> prods(nums.size());

        for(int i = 0; i < nums.size(); ++i)
        {
            int n = nums[i];
            if (n==0)
            {
                if (zeroIdx >= 0)
                {
                    return prods;
                }
                else
                {
                    zeroIdx = i;
                }
            }
            else
            {
                nzProd *= n;
            }
        }


        if (zeroIdx >= 0)
        {
            prods[zeroIdx] = nzProd;
            return prods;
        }
        
        for (int i=0; i<nums.size(); ++i)
        {
            prods[i] = nzProd / nums[i];
        }

        return prods;
    }
};
