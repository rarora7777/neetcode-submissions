class Solution {
public:
    void rotate(vector<vector<int>>& matrix)
    {
        int N = matrix.size();
        if (N==0)
            return;

        vector<vector<int>> m2(N, vector<int>(N));
        for(int i=0; i<N; ++i)
        {
            for (int j=0; j<N; ++j)
            {
                m2[j][N-1-i] = matrix[i][j];
            }
        }

        matrix = m2;
    }
};
