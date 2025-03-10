class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.minHeap=nums
        heapq.heapify(self.minHeap)
        if len(self.minHeap)>k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
