class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        count = {}

        for edge in edges:
            u = edge[0]
            v = edge[1]

            if u not in parent:
                parent[u] = u
                count[u] = 1
            if v not in parent:
                parent[v] = v
                count[v] = 1
            
            while parent[u] != u:
                u = parent[u]
                parent[u] = parent[parent[u]]
            
            while parent[v] != v:
                v = parent[v]
                parent[v] = parent[parent[v]]
            

            if u == v:
                return edge
            elif count[u] >= count[v]:
                parent[v] = u
                count[u] += count[v]
            else:
                parent[u] = v
                count[v] += count[u]
        
        return []

        