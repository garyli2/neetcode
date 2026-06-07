class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            c = frozenset(Counter(s).items())
            if c in anagrams:
                anagrams[c].append(s)
            else:
                anagrams[c] = [s]
        return list(anagrams.values())
