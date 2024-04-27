from typing import List


class Solution:

  def minimumSwaps(self, nums: List[int]) -> int:
    # Find the minimum and maximum numbers in the list
    minNum = min(nums)
    maxNum = max(nums)

    # Initialize the indices of the minimum and maximum numbers
    indexMin = -1
    indexMax = len(nums)

    # Iterate through the list to find the indices of the minimum and maximum numbers
    for i in range(len(nums)):
      if nums[i] == minNum and indexMin == -1:
        indexMin = i
      if nums[i] == maxNum:
        indexMax = i

    # Calculate the minimum number of swaps required
    res = (len(nums) - 1 - indexMax) + indexMin
    # Adjust the result if the index of the maximum number is less than the index of the minimum number
    if indexMax < indexMin:
      res -= 1
    return res
