
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.

# We keep 2 numbers first and second where first < second, and first number must be before second number.
# Iterate num in nums:
# If num <= first then update the first as minimum as possible, byfirst = num
# Else If num <= second then update second as minimum as possible (since now first < num <= second), by second = num
# Else, now first < second < num then we found a valid Increasing Triplet Subsequence, return True.
# Otherwise, return False.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float(inf)

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False