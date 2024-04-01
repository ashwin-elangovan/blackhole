from typing import List


class Solution:

  def firstMissingPositive(self, nums: List[int]) -> int:
    # Append 0 to nums
    # To handle the edge case where elements from 0 to nums_len - 1 are present. Works along the last return statement [1 to nums_len - 1]
    # Sample test case: [1,2,0]
    nums.append(0)

    # Get the length of nums
    nums_len = len(nums)

    # Clear unnecessary values
    for idx in range(nums_len):
      if nums[idx] < 0 or nums[idx] >= nums_len:
        nums[idx] = 0

    # Update values
    for idx in range(nums_len):
      nums[nums[idx] % nums_len] += nums_len

    # Find the first missing positive thats why the range is from 1 not zero
    for idx in range(1, nums_len):
      if nums[idx] // nums_len == 0:
        return idx

    # If all positive integers from 1 to nums_len - 1 are present, return nums_len
    # Sample test case: [1]
    return nums_len
