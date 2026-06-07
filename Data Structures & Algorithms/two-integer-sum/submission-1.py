class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,x in enumerate(nums):
            seen[x] = i
        for i,x in enumerate(nums):
            want = target - x
            if want in seen and seen[want] != i:
                return [i, seen[want]]
        return [-1, -1]