class Solution {
public:
    int maxArea(vector<int>& heights)
    {
        int maxArea = 0;
        // for (int i=0; i<heights.size(); ++i)
        // {
        //     for (int j=i+1; j<heights.size(); ++j)
        //     {
        //         maxArea = max(maxArea, (j-i)*min(heights[i], heights[j]));
        //     }
        // }
        int l = 0;
        int r = heights.size() - 1;

        while(l < r)
        {
            maxArea = max(maxArea, (r-l)*min(heights[l], heights[r]));
            if (heights[l] < heights[r])
            {
                l++;
            }
            else
            {
                r--;
            }
        }

        return maxArea;
    }
};
