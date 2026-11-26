class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        total = 0
        for num in digits:
            total = total * 10 + num
        
        total += 1

        number = []

        while total != 0:
            rem = total % 10 
            number.append(rem)
            total = total // 10 
        
        return number[::-1]

            