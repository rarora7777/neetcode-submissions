class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs)
    {
        // map from sorted character sequence (stored as string) to indices (stored as vector<int>)
        std::unordered_map<string, vector<int>> charsToIdx;

        for (int i=0; i<strs.size(); ++i)
        {
            string chars(strs[i]);
            std::sort(chars.begin(), chars.end());

            if (charsToIdx.contains(chars))
            {
                charsToIdx[chars].push_back(i);
            }
            else
            {
                charsToIdx[chars] = vector<int>({i});
            }
        }


        vector<vector<string>> output;
        output.reserve(charsToIdx.size());

        for(const auto &[chars, idx] : charsToIdx)
        {
            // std::cout<<chars;
            vector<string> entry;
            entry.reserve(idx.size());
            for(const auto& i : idx)
            {
                // std::cout<<' '<<i;
                entry.push_back(strs[i]);
            }
            output.push_back(entry);
            // std::cout<<std::endl;
        }

        return output;
    }
};
