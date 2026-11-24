class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        INF = 200000
        dist = [INF] * n
        k -= 1
        dist[k] = 0

        heapq.heappush(heap, (0, k))

        adj_list = {}
        for i, j, t in times:
            if i-1 not in adj_list:
                adj_list[i-1] = []
            adj_list[i-1].append((j-1, t))

        while heap:
            dist_src, i = heapq.heappop(heap)
            if i not in adj_list:
                continue

            for j, t in adj_list[i]:
                if t + dist_src < dist[j]:
                    dist[j] = t + dist_src
                    # print(f"{j}: {dist[j]} (via {i})")
                    heapq.heappush(heap, (dist[j], j))

        max_dist = max(dist)
        return -1 if max_dist == INF else max_dist