class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges)
    {
        // Create a pointer structure V->V which ultimately points
        // to a unique identifier for each connected component
        vector<int> parent(n);
        // Size of each connected component. Only accurate for the
        // unique identifiers.
        vector<int> count(n, 1);

        for (int i=0; i<n; ++i)
            parent[i] = i;

        int numComp = n;

        for (const auto &e : edges)
        {
            int u = e[0];
            while (parent[u] != u)
            {
                u = parent[u];
                parent[u] = parent[parent[u]];
            }

            int v = e[1];
            while (parent[v] != v)
            {
                v = parent[v];
                parent[v] = parent[parent[v]];
            }

            if (u == v)
                continue;
            
            numComp--;

            if (count[u] >= count[v])
            {
                parent[v] = u;
                count[u] += count[v];
            }
            else
            {
                parent[u] = v;
                count[v] += count[u];
            }
        }

        return numComp;
    }
};
