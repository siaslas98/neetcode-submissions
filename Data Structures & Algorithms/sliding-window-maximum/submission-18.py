class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_heap = []
        ms = {}
        l, r = 0, 0
        n =  len(nums)

        # Expand the window to k elements while adding each element to a max heap.
        while r < k:
            heapq.heappush(max_heap, -nums[r])
            ms[nums[r]] = ms.get(nums[r], 0) + 1
            r += 1
    
        while r < n:
            # Remove max value if its not in s
            while ms[-max_heap[0]] == 0:
                heapq.heappop(max_heap)

            # Append the max value to res list
            if max_heap:
                res.append(-max_heap[0])
            
            # Insert new element to max heap. Expand window by 1 and contract window by 1.
            ms[nums[l]] -= 1
            ms[nums[r]] = ms.get(nums[r], 0) + 1
            heapq.heappush(max_heap, -nums[r])
            l+=1 
            r+=1

        while max_heap and ms[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        if max_heap:
            res.append(-max_heap[0])
        return res

