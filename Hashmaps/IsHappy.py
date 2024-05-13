from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = {}
        
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        for num, count in num_count.items():
            if count == 1:
                return num
        
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            next_num = 0
            while num > 0:
                digit = num % 10
                next_num += digit ** 2
                num //= 10
            return next_num
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
            
        return n == 1 