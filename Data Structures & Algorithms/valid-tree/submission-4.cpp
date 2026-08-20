class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges)
    {
        if (edges.size() != n-1)
            return false;

        vector<vector<int>> adjList(n);
        
        for (const auto& e: edges)
        {
            adjList[e[0]].push_back(e[1]);
            adjList[e[1]].push_back(e[0]);
        }

        vector<bool> visited(n, false);
        // Parent tracking not needed since we're already checking that |E| = |V|-1
        // So we only need to check if the graph is connected
        // vector<int> parent(n, -1);
        queue<int> bfs;

        int root = 0;
        int numVisited = 1;
        visited[root] = true;
        bfs.push(root);

        while (!bfs.empty())
        {
            root = bfs.front();
            bfs.pop();
            // std::cout<<root<<std::endl;
            for(const auto& v: adjList[root])
            {
                if (!visited[v])
                {
                    // parent[v] = root;
                    visited[v] = true;
                    numVisited++;
                    bfs.push(v);
                }
                // else if (parent[root]!=v)
                // {
                //     return false;
                // }
            }
        }

        // check if all vertices visited
        // otherwise we have multiple connectd components in the input graph
        return numVisited == n;
    }
};
