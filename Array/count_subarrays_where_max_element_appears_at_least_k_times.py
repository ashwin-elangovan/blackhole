from typing import List


class Solution:

  def countSubarrays(self, nums: List[int], k: int) -> int:
    # Find the maximum element in the nums list
    max_key = max(nums)

    # Initialize pointers left and right, and variables to keep track of counts
    left, right = 0, 0
    curr_count = 0
    count = 0

    # Loop until the right pointer is within bounds
    while left <= right and right < len(nums):
      # Expand the window until the count of the maximum element (max_key) reaches k
      while right < len(nums) and curr_count < k:
        if nums[right] == max_key:
          curr_count += 1
        right += 1

      # Once the count reaches or exceeds k, calculate the number of subarrays and update count
      while curr_count >= k:
        # Number of subarrays ending at right and having at least k occurrences of max_key is (len(nums) - right + 1)
        count += (len(nums) - right + 1)
        # Move the left pointer and decrement curr_count if nums[left] is equal to max_key
        if nums[left] == max_key:
          curr_count -= 1
        left += 1

    # Return the total count of subarrays satisfying the condition
    return count
