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
        seen = {}  # Dictionary to store the most recent index of each element

        for i, num in enumerate(nums):
            # If the current number is already in the dictionary and the difference
            # between the current index and the previous index of the number is less than or equal to k,
            # then we have found nearby duplicates
            if num in seen and i - seen[num] <= k:
                return True
            # Update the index of the current number in the dictionary
            seen[num] = i

        # If no nearby duplicates were found
        return False
       
    
abc = Solution()
# abc.intersection([1,2,2,1],[2,2])
# print()
