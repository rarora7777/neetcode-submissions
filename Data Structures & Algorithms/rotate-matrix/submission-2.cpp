class Solution {
public:
    void rotate(vector<vector<int>>& matrix)
    {
        int N = matrix.size();
        if (N==0)
            return;

        // vector<vector<int>> m2(N, vector<int>(N));
        // for(int i=0; i<N; ++i)
        // {
        //     for (int j=0; j<N; ++j)
        //     {
        //         m2[j][N-1-i] = matrix[i][j];
        //     }
        // }

        // matrix = m2;

        // Thinking of the matrix as a square, we will rotate the entries at the edges first
        // And then spiral inwards.
        // Example for N=5, * show the active elements in each outer loop
        // *****                 .....                  .....
        // *...* (outer=0) -->   .***. (outer=1) -->    ..... (outer=2)
        // *...*                 .*.*.                  ..*..
        // *...*                 .***.                  .....
        // *****                 .....                  .....
        for (int outer=0; outer<N/2; ++outer)
        {
            int s = outer, e = N-1-outer;
            // Inner goes from the start of each of the four edges to the end
            for(int inner=s; inner<e; ++inner)
            {
                int topLeft = matrix[s][inner];
                // bottom left to top left
                matrix[s][inner] = matrix[e-inner+s][s];
                // bottom right to top right
                matrix[e-inner+s][s] = matrix[e][e-inner+s];
                // top right to bottom right
                matrix[e][e-inner+s] = matrix[inner][e];
                // top left to top right
                matrix[inner][e] = topLeft;
            }
        }
    }
};
