class Solution:
    def countDigits(self, num: int) -> int:
        
        count = 0

        m = num

        while (num != 0):
            remainder = num % 10
            if m % remainder == 0:
                count += 1
            num = num // 10 
        
        return count 