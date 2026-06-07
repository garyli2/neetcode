class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,x in enumerate(nums):
            want = target - x
            if want in seen:
                return [seen[want], i]
            seen[x] = i
        return [-1, -1]