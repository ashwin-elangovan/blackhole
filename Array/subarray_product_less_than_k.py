class Solution:

  def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    # Initialize variables for the current product and count of valid subarrays
    curr_product = 1  # Product of elements in the current subarray
    count = 0  # Count of subarrays with product less than k

    # Initialize left and right pointers for the sliding window
    left, right = 0, 0

    # Iterate through the array using the sliding window technique
    while right < len(nums):
      # Update the current product by multiplying with the element at the right pointer
      curr_product *= nums[right]

      # Shrink the window from the left until the product is less than k
      while curr_product >= k and left <= right:
        curr_product /= nums[left]  # Divide by the element at the left pointer
        left += 1  # Move the left pointer forward

      # Update the count by adding the number of valid subarrays in the current window
      # The count is incremented by the length of the subarray from left to right (inclusive)
      count += right - left + 1

      # Move the right pointer forward to expand the window
      right += 1

    # Return the total count of subarrays with product less than k
    return count
