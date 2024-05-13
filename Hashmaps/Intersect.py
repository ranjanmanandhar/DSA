from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
            rslt = []
            for num2 in nums2:
                if num2 in nums1:
                    rslt.append(num2)
                    nums1.remove(num2)
            return rslt

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        # Find the intersection using set intersection operation
        intersection = nums1.intersection(nums2)
        
        # Convert the intersection set back to a list
        return list(intersection)
    
abc = Solution()
# abc.intersection([1,2,2,1],[2,2])
   