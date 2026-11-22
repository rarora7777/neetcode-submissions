class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_pts = []
        
        for pt in points:
            heapq.heappush_max(dist_pts, (pt[0]*pt[0] + pt[1]*pt[1], pt))
            if len(dist_pts) > k:
                heapq.heappop_max(dist_pts)
        
        return [pair[1] for pair in dist_pts]