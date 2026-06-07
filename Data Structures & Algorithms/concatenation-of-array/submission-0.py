class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (2 * n)
        for i,x in enumerate(nums):
            result[i] = x
            result[i+n] = x
        return result