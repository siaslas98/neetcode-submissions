class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # iterate through the list of points
        # add the point into visited set
        # find the manhattan distance between the first point and every other point and push each distance into
        # a min heap
        # to choose the next point to add to visited, just pop from the min heap

        distances = []
        res = 0
        unvisited = set(range(1, len(points)))

        xi, yi = points[0]
        for i in range(1, len(points)):
            xj, yj = points[i]
            heapq.heappush(distances, (abs(xi-xj) + abs(yi-yj), i))

        while unvisited:
            distance, idx = heapq.heappop(distances)

            if idx not in unvisited:
                continue

            res += distance
            unvisited.remove(idx)

            xi, yi = points[idx]
            for k in unvisited:
                xj, yj = points[k]
                heapq.heappush(distances, (abs(xi-xj) + abs(yi-yj), k))
        
        return res