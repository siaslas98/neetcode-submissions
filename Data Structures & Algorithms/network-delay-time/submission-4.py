class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Convert times(edge list) to adjacency list
        nodes = {}

        for time in times:
            ui, vi, ti = time
            if ui in nodes:
                nodes[ui].append((vi,ti))
            else:
                nodes[ui] = [(vi, ti)]
            if vi not in nodes:
                nodes[vi] = []
                
        if len(nodes) != n:
            return -1

        # Helps to retrieve shortest dv node
        dist = {node: float('inf') for node in nodes}
        dist[k] = 0
        prev = {node: None for node in nodes}

        pq = [(0, k)]

        while pq:
            d, u = heapq.heappop(pq)

            for v, w in nodes[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        
        res = -1
        for d in dist:
            if dist[d] == float('inf'):
                return -1
            res = max(res, dist[d])
        
        return res 
            
