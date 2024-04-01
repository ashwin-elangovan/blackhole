from typing import List


class Solution:

  def sortColors(self, nums: List[int]) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """
    # Initialize three pointers low, mid, and high
    low, mid, high = 0, 0, len(nums) - 1

    # Loop until mid pointer crosses the high pointer
    while mid <= high:
      # If the element at mid pointer is 0, swap it with the element at low pointer
      # Move both low and mid pointers to the right
      if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
      # If the element at mid pointer is 1, simply move the mid pointer to the right
      elif nums[mid] == 1:
        mid += 1
      # If the element at mid pointer is 2, swap it with the element at high pointer
      # Move the high pointer to the left
      elif nums[mid] == 2:
        nums[high], nums[mid] = nums[mid], nums[high]
        high -= 1

    # Note: We are not returning anything as the modification is done in-place on nums
