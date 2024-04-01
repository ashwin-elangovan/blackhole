from collections import defaultdict
from typing import List


class Solution:

  def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    # Define a helper function to count subarrays with at most k distinct elements
    def almost(nums, k):
      left, right = 0, 0
      arr_count = 0
      count_hash = defaultdict(
        lambda: 0
      )  # Initialize a defaultdict to store the count of each element

      while right < len(nums):
        count_hash[
          nums[right]] += 1  # Update count of elements as we expand the window

        # Shrink the window if the number of distinct elements exceeds k
        while len(count_hash.keys()) > k:
          count_hash[
            nums[left]] -= 1  # Decrease count of the element at the left end
          if count_hash[nums[
              left]] == 0:  # If count becomes zero, remove the element from the dictionary
            del count_hash[nums[left]]
          left += 1  # Move the left pointer to the right

        arr_count += right - left + 1  # Update the count of subarrays ending at the current 'right' index
        right += 1  # Move the right pointer to the right

      return arr_count  # Return the count of subarrays with at most k distinct elements

    # The total count of subarrays with exactly k distinct elements is equal to the difference
    # between the count of subarrays with at most k distinct elements and the count of subarrays
    # with at most (k-1) distinct elements
    return almost(nums, k) - almost(nums, k - 1)
