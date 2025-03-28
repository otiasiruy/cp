class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            if s[l] != s[r]:
                return checkPalindrome(l + 1, r) or checkPalindrome(l, r - 1)
            l += 1
            r -= 1
        return True