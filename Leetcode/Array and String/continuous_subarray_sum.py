# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

# A good subarray is a subarray where:

# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:

# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

# Logic: Check for the prvious entry with the same remainder. Thats means between 2 indexes there is a sibarray with sum as multiple of k. If the difference between the current index and the previous index is greater than 2, then we have a subarray with sum as multiple of k.
 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Create a dictionary to store the remainder (0 is remainder) and its corresponding index
        sum_dict = {0: -1}  # 0 is remainder and -1 is index coz we have to handle if the first element itself id divisible by k

        curr_sum = 0  # Initialize the current sum to 0

        for idx, num in enumerate(nums):
            curr_sum += num  # Add the current number to the current sum

            remainder = curr_sum % k  # Calculate the remainder of the current sum when divided by k

            # Check if the remainder is not already in the sum_dict
            if remainder not in sum_dict:
                sum_dict[remainder] = idx  # If not, add it to the dictionary with the current index
            # If the remainder is already in the sum_dict, check if the difference between
            # the current index and the index stored in sum_dict is greater than or equal to 2
            elif (idx - sum_dict[remainder]) >= 2:
                return True  # If yes, return True as we found a good subarray

        return False  # If no good subarray is found, return False
