class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = [0] * 26
        tArr = [0] * 26
        for c in s: sArr[ord(c) - ord('a')] += 1
        for c in t: tArr[ord(c) - ord('a')] += 1
        return sArr == tArr