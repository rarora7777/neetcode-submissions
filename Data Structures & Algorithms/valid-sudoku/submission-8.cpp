class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board)
    {
        vector<vector<bool>> rowFreq(9);
        vector<vector<bool>> colFreq(9);
        vector<vector<bool>> blkFreq(9);

        for (int i=0; i<9; ++i)
        {
            rowFreq[i] = vector<bool>(9);
            colFreq[i] = vector<bool>(9);
            blkFreq[i] = vector<bool>(9);
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

                if (rowFreq[r][num] || colFreq[c][num] || blkFreq[b][num])
                {
                    return false;
                }

                rowFreq[r][num] = true;
                colFreq[c][num] = true;
                blkFreq[b][num] = true;
            }
        }

        return true;
    }
};
