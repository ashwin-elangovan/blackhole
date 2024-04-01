from typing import List


class Solution:

  def findDuplicate(self, nums: List[int]) -> int:
    # Iterate through each number in the list
    for num in nums:
      # Get the absolute value of the current number to avoid indexing issues
      curr_num = abs(num)  # To avoid unnecessary conflicts

      # Check if the number at the current index (curr_num) is negative
      # If it's negative, it means curr_num has been encountered before
      if nums[curr_num - 1] < 0:
        # Return the current number (curr_num) which is the duplicate
        return curr_num

      # Mark the number at the current index (curr_num) as visited by making it negative
      nums[curr_num - 1] = -nums[curr_num - 1]
      # -1 is added such that 1 will correspond to nums[0], 2 will correspond to nums[1]