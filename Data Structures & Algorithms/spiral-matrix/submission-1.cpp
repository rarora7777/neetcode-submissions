class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix)
    {
        int M = matrix.size();

        if (M==0)
            return vector<int>();
        int N = matrix[0].size();

        vector<int> vec(M*N);
        int idx = 0;

        int numLoop = min(M, N)/2;

        // Spiral can be subdivided into CW loops starting at the top-left
        for (int loop=0; loop<numLoop; ++loop)
        {
            for (int i=loop; i<N-1-loop; ++i)
                vec[idx++] = matrix[loop][i];
            
            for (int i=loop; i<M-1-loop; ++i)
                vec[idx++] = matrix[i][N-1-loop];

            for (int i=N-1-loop; i>loop; --i)
                vec[idx++] = matrix[M-1-loop][i];
            
            for (int i=M-1-loop; i>loop; --i)
                vec[idx++] = matrix[i][loop];
        }

        // Add remaining row or column
        if (M>=N && N%2==1)
        {
            // Add row
            for(int i=numLoop; i<M-numLoop; ++i)
                vec[idx++] = matrix[i][numLoop];
        }
        else if (N>M && M%2==1)
        {
            // Add column
            for(int i=numLoop; i<N-numLoop; ++i)
                vec[idx++] = matrix[numLoop][i];
        }

        return vec;
    }
};
