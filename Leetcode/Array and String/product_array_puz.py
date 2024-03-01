# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
# Example 2:

# Input: nums = [-1, 1, 0, -3, 3]
# Output: [0, 0, 9, 0, 0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create an array 'fin' of the same length as 'nums' with all elements initialized to 1.
        fin = [1 for i in nums]
        
        temp = 1  # Initialize a variable 'temp' to store the product of elements on the left side.
        n = len(nums)  # Get the length of the input array 'nums'.
        
        # Calculate the product of elements on the left side of each element.
        for i in range(n):
            fin[i] *= temp  # Multiply the current value in 'fin' with 'temp'.
            temp *= nums[i]  # Update 'temp' with the product of the current element.

        temp = 1  # Reset 'temp' to 1 for the next loop iteration.

        # Calculate the product of elements on the right side of each element.
        for i in range(n - 1, -1, -1):
            fin[i] *= temp  # Multiply the current value in 'fin' with 'temp'.
            temp *= nums[i]  # Update 'temp' with the product of the current element.

        return fin  # Return the final array 'fin' containing the product of all elements except the current element.
