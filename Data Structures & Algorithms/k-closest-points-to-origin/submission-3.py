class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        heapq.heapify(distances)
        res: List[List[int]] = []

        for idx, point in enumerate(points):
            x, y = point
            heapq.heappush(distances, [-math.sqrt(x**2 + y**2), idx])
            if len(distances) > k:
                heapq.heappop(distances)
        
        for distance in distances:
            res.append(points[distance[1]])

        return res
        
        

