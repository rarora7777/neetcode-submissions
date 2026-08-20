class Solution {
public:
    bool isPalindrome(string s)
    {
        int left = 0;
        int right = s.length()-1;

        // std::transform(s.begin(), s.end(), s.begin(), [](char ch) {return std::tolower(ch);});

        auto isalphnum = [](char ch)
        {
            return (ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9');
        };

        while (left < right)
        {
            while (left < right && !isalphnum(s[left]))
            {
                left++;
                continue;
            }
            while (left < right && !isalphnum(s[right]))
            {
                right--;
                continue;
            }
            if (std::tolower(s[left]) != std::tolower(s[right]))
            {
                return false;
            }

            left++;
            right--;
        }
        
        return true;
    }
};
