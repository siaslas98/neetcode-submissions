class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = {}

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        heap = []

        for num, count in frequencies.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for num in heap:
            res.append(num[1])
        
        return res





