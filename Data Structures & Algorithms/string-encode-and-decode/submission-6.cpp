class Solution {
public:

    string encode(vector<string>& strs)
    {
        vector<char> chars;
        int nextZeroIdx;
        for(const auto& str : strs)
        {
            nextZeroIdx = chars.size();
            chars.push_back(0);
            for (const auto& ch : str)
            {
                chars.push_back(ch);
            }
            chars[nextZeroIdx] = str.length() + 1;
        }
        chars.push_back(0);

        string output(chars.begin(), chars.end());
        std::cout<<output;

        return output;
    }

    vector<string> decode(string s)
    {
        vector<string> decoded;

        int idx = 1;
        while (idx < s.length())
        {
            uint8_t strlen = s[idx-1];
            decoded.push_back(s.substr(idx, strlen - 1));
            idx += strlen;
        }

        return decoded;
    }
};
