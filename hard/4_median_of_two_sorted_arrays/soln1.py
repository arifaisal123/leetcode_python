class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums1 = nums1
        self.nums2 = nums2
        
        merged_array = nums1 + nums2
        merged_array.sort()

        if len(merged_array) % 2 != 0: # Odd
            median_index = (len(merged_array) - 1) // 2
            final_median = (merged_array[median_index])
            return final_median

        else:
            median_index = (len(merged_array) - 1) // 2
            final_median = (merged_array[median_index] + merged_array[median_index + 1]) / 2
            return final_median        
        