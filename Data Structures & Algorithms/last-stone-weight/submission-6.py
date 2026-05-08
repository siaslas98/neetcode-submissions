class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We want to use a max heap
        self.heap = []

        def heapifyUp(heap):
            child = len(heap)-1


            while True:
                if child == 0:
                    return 
                parent = (child - 1) // 2
                if heap[parent] < heap[child]:
                    heap[parent], heap[child] = heap[child], heap[parent]
                child = parent

        def heapifyDown(heap):
            parent = 0

            while True:
                childLeft = 2 * parent + 1
                childRight = 2 * parent + 2
                max_idx = parent

                if childLeft < len(heap) and heap[childLeft] > heap[max_idx]:
                    max_idx = childLeft
                if childRight < len(heap) and heap[childRight] > heap[max_idx]:
                    max_idx = childRight
                
                if max_idx == parent:
                    break
                
                heap[parent], heap[max_idx] = heap[max_idx], heap[parent]
                parent = max_idx
                
        def pop(heap):
            heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
            ret_val = heap.pop()
            heapifyDown(heap)
            return ret_val
        
        for stone in stones:
            self.heap.append(stone)
            heapifyUp(self.heap)
        
        while len(self.heap) > 1:
            firstLargest = pop(self.heap)
            secondLargest = pop(self.heap)

            res = abs(firstLargest-secondLargest)
            
            if res != 0:
                self.heap.append(res)
                heapifyUp(self.heap)
        
        return self.heap[0] if self.heap else 0
            



        
        
