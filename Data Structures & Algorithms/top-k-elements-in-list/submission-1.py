class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [None] * len(nums)
        c = Counter(nums)
        for (x, n) in c.items():
            if freqs[n-1] is None: freqs[n-1] = []
            freqs[n-1].append(x)
        found = 0
        results = []
        for i in range(len(nums)-1, -1, -1):
            if found >= k: break
            if freqs[i] is None: continue
            for n in freqs[i]: results.append(n)
            found += len(freqs[i])
        return results
