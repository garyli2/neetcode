class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        index = 0
        while True:
            if index >= len(strs[0]): return result
            curChar = strs[0][index]
            for s in strs:
                if index >= len(s): return result
                if s[index] != curChar: return result
            result += curChar
            index += 1
        return result