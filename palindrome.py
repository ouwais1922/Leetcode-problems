def isPalindrome( x: int) -> bool:
     if x < 0:
        return False
        toString = str(x)
        return toString == toString[::-1]

# try without converted to a string

print(isPalindrome(121))


## without converting to string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverseNumber = 0
        firstValue = x
        while x > 0:
            lastDigit = x % 10
            reverseNumber = reverseNumber * 10 + lastDigit
            x = x // 10
        return firstValue == reverseNumber

# lets take : 121
# lastDigit = 1
# reverseNumber = 0 * 10 + 1 = 1
# x = 121 // 10 = 12