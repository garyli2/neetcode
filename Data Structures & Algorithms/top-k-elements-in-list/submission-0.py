class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        minHeap = []
        for (x, n) in c.items():
            if len(minHeap) >= k:
                if n > minHeap[0][0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (n, x))
            else:
                heapq.heappush(minHeap, (n, x))
        return [a[1] for a in minHeap]

