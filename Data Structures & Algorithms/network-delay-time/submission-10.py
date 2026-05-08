class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = {i: [] for i in range(1, n+1)}
    
        for u, v, t in times:
            adjList[u].append((v, t))

        du = {}
        pv = {}

        for node in adjList:
            if node == k:
                du[node] = 0
            else:
                du[node] = float('inf')
            pv[node] = None
        

        visited = set()
        q = [(dist, node) for node, dist in du.items()]
        heapq.heapify(q)

        while q:
            d1, node = heapq.heappop(q)
            visited.add(node)

            for pair in adjList[node]:
                neighbor, d2 = pair
                alt = d1 + d2
                if neighbor not in visited and alt < du[neighbor]:
                    du[neighbor] = alt
                    pv[neighbor] = node
                    heapq.heappush(q, (alt, neighbor))
        
        maxDist = max(du.values())
        if maxDist == float('inf'):
            return -1
        return maxDist






        

