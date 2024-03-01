# Given a binary array 'nums' and an integer 'k', the task is to return the maximum number of consecutive 1's in the array.
# You can flip at most 'k' 0's to 1's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Given a binary array 'A' and an integer 'K', the task is to return the maximum number of consecutive 1's in the array.
# You can flip at most 'K' 0's to 1's.

# Explanation: https://leetcode.com/problems/max-consecutive-ones-iii/solutions/719833/python3-sliding-window-with-clear-example-explains-why-the-soln-works/

class Solution:
    def longestOnes(self, nums: List[int], K: int) -> int:
        left = 0  # Initialize left pointer.

        for right, value in enumerate(nums):
            # If we encounter a 0, then we decrement 'K'.
            if value == 0:
                K -= 1
            # Fancy way of doing this
            # k -= (1 - value)
            # If it's a 1, there is no impact on 'K'.

            # If 'K' becomes negative, we need to move the left part of the window forward
            # to try and remove the extra 0's.

            # HINT: Only when k is zero or greater than zero, left pointer stays still and we can maximize the window size. 
            # Else the left pointer moves along the right pointer which will retain the current maximum window size
            # ANd thats why we dont need to keep track of the maximum window size and just do right - left + 1 which is the max size found so far.
            # The max size need not be the window size of the current elements.
            if K < 0:
                # If the left one was a zero, then we adjust 'K'. Only if k is not negative right pointer will expand the window size. Else left pointer will catchup with that.
                if nums[left] == 0:
                    K += 1
                # Fancy way of doing this: k += (1 - nums[left])
                # Regardless of whether we had a 1 or a 0, we can move the left pointer by 1.
                # If we keep seeing 1's, the window still keeps moving as-is.
                left += 1
        
        # The final 'right' position minus the 'left' position gives the size of the longest subarray of 1's.
        # Adding 1 because both 'left' and 'right' are zero-based indices.
        return right - left + 1
