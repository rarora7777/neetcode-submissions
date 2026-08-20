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
            int pu = parent[u];
            while (pu != u)
            {
                u = pu;
                pu = parent[pu];
            }

            int v = e[1];
            int pv = parent[v];
            while (pv != v)
            {
                v = pv;
                pv = parent[pv];
            }

            if (pu == pv)
                continue;
            
            numComp--;

            // if (count[pu] >= count[pv])
            {
                parent[pv] = pu;
                count[pu] += count[pv];
            }
            // else
            // {
            //     parent[pu] = pv;
            //     count[pv] += count[pu];
            // }
        }

        return numComp;
    }
};
