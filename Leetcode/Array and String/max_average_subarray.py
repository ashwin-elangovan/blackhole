# You are given an integer array 'nums' consisting of 'n' elements, and an integer 'k'.
# The goal is to find a contiguous subarray whose length is equal to 'k' that has the maximum average value and return this value.
# Any answer with a calculation error less than 10^-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Check if 'k' is greater than the length of 'nums'.
        # If so, a contiguous subarray of length 'k' cannot be formed, and return None.
        if k > len(nums):
            return None
        
        # Initialize 'final_sum' and 'temp_sum' to the sum of the first 'k' elements.
        final_sum = temp_sum = sum(nums[:k])
        
        # Iterate through the array starting from the index 'k'.
        for i in range(k, len(nums)):
            # Update 'temp_sum' by adding the current element and subtracting the element 'k' positions earlier.
            temp_sum += nums[i] - nums[i - k]
            
            # Update 'final_sum' with the maximum of 'temp_sum' and the existing 'final_sum'.
            final_sum = max(temp_sum, final_sum)

        # Return the maximum average by dividing 'final_sum' by 'k'.
        return final_sum / k
