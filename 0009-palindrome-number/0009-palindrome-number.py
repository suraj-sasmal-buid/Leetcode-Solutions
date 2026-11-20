class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = str(x)

        for i in range(len(n)):
            if n == n[::-1]:
                return True
            else:
                return False