class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        
        for key in s:
            sd[key] = sd.get(key, 0) + 1
        for key in t:
            td[key] = td.get(key, 0) + 1
        if sd == td:
            return True
        return False
        