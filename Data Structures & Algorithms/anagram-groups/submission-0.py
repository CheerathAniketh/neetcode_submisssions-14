class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for words in strs:
            sortwords = sorted(words)
            key = "".join(sortwords)
            if key not in dict:
                dict[key] = []

            dict[key].append(words)
        return list(dict.values())