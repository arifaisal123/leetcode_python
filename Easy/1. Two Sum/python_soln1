class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for idx, num in enumerate(nums):
            if (target-num) in hash_map:
                return [idx, hash_map[target-num]]
            hash_map[num] = idx  
            
