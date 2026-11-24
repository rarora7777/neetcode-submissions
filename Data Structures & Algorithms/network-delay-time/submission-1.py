class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        heapq.heappush(heap, (0, k))
        visited = set()

        adj_list = {}
        for i, j, t in times:
            if i not in adj_list:
                adj_list[i] = []
            adj_list[i].append((j, t))

        max_dist = 0
        while heap:
            dist_src, i = heapq.heappop(heap)
            if i in visited:
                continue

            visited.add(i)
            # print("visited", i)
            max_dist = dist_src

            if i not in adj_list:
                continue

            for j, t in adj_list[i]:
                if j not in visited:
                    # print(f"{j}: {dist_src + t} (via {i})")
                    heapq.heappush(heap, (dist_src + t, j))

        return max_dist if len(visited) == n else -1