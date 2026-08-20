class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board)
    {
        vector<vector<int>> rowFreq(9);
        vector<vector<int>> colFreq(9);
        vector<vector<int>> blkFreq(9);

        for (int i=0; i<9; ++i)
        {
            rowFreq[i] = vector<int>(9);
            colFreq[i] = vector<int>(9);
            blkFreq[i] = vector<int>(9);
        }

        for (int r=0; r<9; ++r)
        {
            for (int c=0; c<9; ++c)
            {
                if (board[r][c] == '.')
                {
                    continue;
                }
                
                int b = r / 3 + 3 * (c / 3);
                int num = board[r][c] - '1';
                std::cout<<r<<' '<<c<<' '<<b<<' '<<num<<std::endl;
                rowFreq[r][num]++;
                colFreq[c][num]++;
                blkFreq[b][num]++;

                if (rowFreq[r][num] > 1 || colFreq[c][num] > 1 || blkFreq[b][num] > 1)
                {
                    return false;
                }
            }
        }

        return true;
    }
};
