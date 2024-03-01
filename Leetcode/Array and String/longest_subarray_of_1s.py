# Given a binary array 'nums', you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# Return 0 if there is no such subarray.

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with a value of 1's.

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with a value of 1's is [1,1,1,1,1].

# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0               # Initialize the left pointer.
        max_window = 0         # Initialize the variable to store the maximum subarray length.
        last_zero = -1         # Initialize the index of the last zero encountered.

        for right in range(len(nums)):
            if nums[right] == 0:
                left = last_zero + 1    # Update the left pointer to the position after the last zero.
                last_zero = right       # Update the index of the current zero encountered. So next time, left will become current_zero + 1
            
            # Update the 'max_window' with the maximum of the current window length and the existing maximum.
            max_window = max(max_window, right - left)
        
        return max_window  # Return the size of the longest non-empty subarray containing only 1's.
