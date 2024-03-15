class Solution:
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
      # Initialize a dictionary to store the prefix sum frequencies
      prefix_sum = defaultdict(lambda: 0)
      # Initialize the prefix sum 0 with frequency 1, which represents an empty subarray
      prefix_sum[0] = 1
      # Initialize the current count and the final result
      curr_count = 0
      final_val = 0
      # Iterate through the numbers in the list
      for num in nums:
          # Update the current count by adding the current number
          curr_count += num
          # Check if there exists a prefix sum such that (current_sum - goal) = prefix_sum
          # If such a prefix sum exists, it means there is a subarray that sums up to the goal
          if curr_count - goal in prefix_sum:
              # Add the frequency of the prefix sum to the final result
              final_val += prefix_sum[curr_count - goal]
          # Increment the frequency of the current prefix sum in the dictionary
          prefix_sum[curr_count] += 1
      # Return the final result
      return final_val
