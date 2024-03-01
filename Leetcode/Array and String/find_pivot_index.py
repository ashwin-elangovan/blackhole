# Given an array of integers 'nums', the task is to calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
# This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation: The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation: There is no index that satisfies the conditions in the problem statement.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Calculate the total sum of all elements in the array.
        left_sum = 0  # Initialize the left sum.

        # Loop through the array using enumerate to access both the index 'idx' and the value 'val'.
        for idx, val in enumerate(nums):
            # If the left sum is equal to the sum of elements to the right of the current index, return the index.
            if left_sum == (total_sum - left_sum - val):
                return idx
            left_sum += val  # Add the current value to the left sum.

        return -1  # If no pivot index is found, return -1.
