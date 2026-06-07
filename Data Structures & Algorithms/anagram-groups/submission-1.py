class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            freq = [0] * 26
            for c in s: freq[ord(c)-ord('a')] += 1
            key = ",".join([str(a) for a in freq])
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
        return list(anagrams.values())
