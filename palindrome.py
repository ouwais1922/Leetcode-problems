class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        toString = str(x)
        return toString == toString[::-1]

# try without converted to a string