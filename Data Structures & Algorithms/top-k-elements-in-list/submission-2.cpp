class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k)
    {
        unordered_map<int, int> numCount;
        for (const auto &n : nums)
        {
            if (numCount.contains(n))
            {
                numCount[n]++;
            }
            else
            {
                numCount[n] = 1;
            }
        }

        std::vector<std::pair<int, int>> numCountVec;
        numCountVec.reserve(numCount.size());

        for(const auto &[key, value] : numCount)
        {
            numCountVec.push_back(std::pair<int, int>(key, value));
        }

        sort(numCountVec.begin(), numCountVec.end(), 
            [](std::pair<int, int> kv1, std::pair<int, int> kv2)
            {
                return kv1.second > kv2.second;
            }
        );

        vector<int> output(k);
        for(int i=0; i<k; ++i)
        {
            output[i] = numCountVec[i].first;
        }

        return output;
    }
};
