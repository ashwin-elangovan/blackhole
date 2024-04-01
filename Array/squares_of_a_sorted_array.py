from typing import List
from collections import deque


class Solution:

  def sortedSquares(self, nums: List[int]) -> List[int]:
    # Initialize a deque to store the final squared and sorted values
    final_arr = deque()

    # Initialize pointers for the two ends of the input array
    left = 0
    right = len(nums) - 1

    # Iterate until both pointers meet or cross each other
    while left <= right:
      # Compare the absolute values of the elements at the two ends
      if abs(nums[left]) >= abs(nums[right]):
        # If the absolute value of the element at the left pointer is greater or equal,
        # square it and append it to the left of the deque
        final_arr.appendleft(nums[left] * nums[left])
        # Move the left pointer to the right
        left += 1
      else:
        # If the absolute value of the element at the right pointer is greater,
        # square it and append it to the left of the deque
        final_arr.appendleft(nums[right] * nums[right])
        # Move the right pointer to the left
        right -= 1

    # Return the list converted from the deque, which contains squared and sorted values
    return list(final_arr)
