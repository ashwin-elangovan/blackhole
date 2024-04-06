from typing import List


class Solution:

  def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
    start = 0  # Initialize the starting index of the current subarray
    maxFound = False  # Flag to track if maxK has been found in the current subarray
    minFound = False  # Flag to track if minK has been found in the current subarray
    minStart = 0  # Index where minK was found in the current subarray
    maxStart = 0  # Index where maxK was found in the current subarray
    count = 0  # Counter to track the number of valid subarrays

    for idx in range(len(nums)):
      curr_num = nums[idx]  # Current number in the array at index idx

      # If the current number is outside the range [minK, maxK]
      if curr_num > maxK or curr_num < minK:
        minFound = False  # Reset minFound flag
        maxFound = False  # Reset maxFound flag
        start = idx + 1  # Update the start index for the next subarray

      # If the current number equals minK, update minFound flag and minStart index
      if curr_num == minK:
        minFound = True
        minStart = idx

      # If the current number equals maxK, update maxFound flag and maxStart index
      if curr_num == maxK:
        maxFound = True
        maxStart = idx

      # If both minK and maxK have been found in the current subarray
      if minFound and maxFound:
        # Update the count by the length of the current subarray
        count += min(minStart, maxStart) - start + 1

    return count  # Return the total count of valid subarrays
