from typing import List


class Solution:

  def findDuplicates(self, nums: List[int]) -> List[int]:
    # Initialize an empty list to store the duplicate elements
    final_arr = []

    # Iterate through the elements and their indices in the input list nums
    for idx, num in enumerate(nums):
      # Calculate the index corresponding to the current number (taking absolute value to handle negatives)
      curr_idx = abs(num) - 1

      # Check if the number at the calculated index is negative
      if nums[curr_idx] < 0:
        # If it's negative, it means the number has been encountered before
        # Add the absolute value of the current number (the duplicate) to the final array
        final_arr.append(abs(num))

      # Mark the number at the calculated index as visited by negating it
      nums[curr_idx] = -nums[curr_idx]

    # Return the list containing the duplicate elements
    return final_arr
