"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupl_dict = dict()
        
        for idx, num in enumerate(nums):
            if num in dupl_dict and idx - dupl_dict[num] <= k:
                return True
            dupl_dict[num] = idx
        return False
                    