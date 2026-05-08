class KthLargest:

    @staticmethod
    def heapifyUp(heap):
        cur_idx = len(heap)-1
        parent = (cur_idx - 1) // 2

        while parent >= 0 and heap[cur_idx] < heap[parent]:
            heap[cur_idx], heap[parent] = heap[parent], heap[cur_idx]
            cur_idx = parent
            parent = (cur_idx - 1) // 2
    
    @staticmethod
    def heapifyDown(heap, size, parent):
        childL = (parent * 2) + 1
        childR = (parent * 2) + 2

        if childL < size and heap[parent] > heap[childL]:
            heap[childL], heap[parent] = heap[parent], heap[childL]
            KthLargest.heapifyDown(heap, size, childL)

        if childR < size and heap[parent] > heap[childR]:
            heap[childR], heap[parent] = heap[parent], heap[childR]
            KthLargest.heapifyDown(heap, size, childR)

    @staticmethod
    def popHeap(nums, size):
        nums[0], nums[len(nums)-1] = nums[len(nums)-1], nums[0]
        KthLargest.heapifyDown(nums, size, 0)


    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.nums = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.heapifyUp(self.nums)
        if len(self.nums) > self.size:
            self.popHeap(self.nums, self.size)
            self.nums.pop()
        return self.nums[0]
        
