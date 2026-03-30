class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for i in s:
            if i.isalnum():
                clean = clean+i.lower()
    
        cleanprime = clean[::-1]
        if clean == cleanprime:
            return True
        return False