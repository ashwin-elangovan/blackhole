from collections import defaultdict


class Solution:

  def subarraySum(self, nums: List[int], k: int) -> int:
    # Dictionary to store the cumulative sums and their frequencies
    sum_set = defaultdict(lambda: 0)

    # Variable to store the final count of subarrays with sum equal to k
    final_count = 0

    # Variable to keep track of the cumulative sum
    curr_sum = 0

    # Iterate through the elements of the array
    for num in nums:
      # Update the cumulative sum
      curr_sum += num

      # If the current sum equals k, increment the final count
      if curr_sum == k:
        final_count += 1

      # If the difference between the current sum and k exists in the sum_set,
      # increment the final count by the frequency of that difference
      if curr_sum - k in sum_set:
        final_count += sum_set[curr_sum - k]

      # Increment the frequency of the current sum in the sum_set
      sum_set[curr_sum] += 1

    # Return the final count of subarrays with sum equal to k
    return final_count
