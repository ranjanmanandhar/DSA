from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
       
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
            
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1 = set(nums1)
        nums2 = set(nums2)
         # Find the intersection using set intersection operation
        intersection = nums1.intersection(nums2)
        
        # Convert the intersection set back to a list
        return list(intersection)
        
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
    
abc = Solution()
# abc.intersection([1,2,2,1],[2,2])
# print()
a = abc.isHappy(33)
print(a)