# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        length = len(nums)
        sorted_val = sorted(nums)
        largest_num = sorted_val[length-1] # Largest number
        s_largest_num = sorted_val[length-2] # second largest number
        if largest_num >= 2*s_largest_num:
            return nums.index(largest_num)
        return -1

