class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums)
    {
        // product of non-zero elements
        int nzProd = 1;
        // index of first zero in nums
        int zeroIdx = -1;

        vector<int> prods(nums.size());

        for(int i = 0; i < nums.size(); ++i)
        {
            int n = nums[i];
            if (n==0)
            {
                if (zeroIdx >= 0)
                {
                    // If nums has 2 or more zeroes, then product of nums {0..n} \ {i} is zero for all i
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

        // if there is exactly one 0 in nums, then the product at that index is non-zero, the rest are all zeros.
        if (zeroIdx >= 0)
        {
            prods[zeroIdx] = nzProd;
            return prods;
        }
        
        // "usual" case with no zeros in the list
        for (int i=0; i<nums.size(); ++i)
        {
            prods[i] = nzProd / nums[i];
        }

        return prods;
    }
};
