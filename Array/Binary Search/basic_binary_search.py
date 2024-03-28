class Solution:

  def search(self, nums: List[int], target: int) -> int:
    # Initialize the left and right pointers
    left, right = 0, len(nums)

    # Loop until the left pointer crosses the right pointer
    while left < right:
      # Calculate the mid index using the left and right pointers
      mid = left + (right - left) // 2

      # Check if the element at the mid index is equal to the target
      if nums[mid] == target:
        return mid
      # If the element at the mid index is greater than the target,
      # adjust the right pointer to search the left half of the array
      elif nums[mid] > target:
        right = mid
      # If the element at the mid index is less than the target,
      # adjust the left pointer to search the right half of the array
      else:
        left = mid + 1

    # If the target is not found, return -1
    return -1
