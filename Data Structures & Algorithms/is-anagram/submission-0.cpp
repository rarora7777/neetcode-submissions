class Solution {
public:
    std::map<char, int> getCharCount(string s)
    {
        std::map<char, int> sCount;

        for(const auto &ch : s)
        {
            if (sCount.contains(ch))
            {
                sCount[ch]++;              
            }
            else
            {
                sCount[ch] = 0;
            }
        }

        return sCount;
    }

    bool isAnagram(string s, string t)
    {
        std::map<char, int> sCount = getCharCount(s);
        std::map<char, int> tCount = getCharCount(t);

        return sCount == tCount;
    }
};
