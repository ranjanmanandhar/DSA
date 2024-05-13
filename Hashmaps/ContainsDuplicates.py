from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = 1
        
        for num in nums:
            if num == k:
                counter += 1
        
        if counter > 1 and counter % 2 == 0:
            return True
        
        return False
       
    
abc = Solution()
# abc.intersection([1,2,2,1],[2,2])
# print()
