class Solution:

  def printLIS(self, dp: List[int], nums: List[int]) -> None:
    # Find the maximum value in the dp array, which represents the length of the Longest Increasing Subsequence (LIS)
    end = max(dp)
    # Find the index of the last element of the LIS in the original nums array
    end_idx = dp.index(end)
    # Initialize an array to store the elements of the LIS
    final_arr = [nums[end_idx]]
    # Iterate backwards from the end index of the LIS in the dp array
    for idx in range(end_idx - 1, -1, -1):
      # If the current index is less than the end index and the value of dp[idx] plus 1 equals dp[end_idx],
      # it means nums[idx] is part of the LIS
      if idx < end_idx and dp[idx] + 1 == dp[end_idx]:
        # Append nums[idx] to the final_arr
        final_arr.append(nums[idx])
        # Update the end index to the current index
        end_idx = idx
    # Print the elements of the LIS in reverse order
    print(final_arr[::-1])
    return None

  def lengthOfLIS(self, nums: List[int]) -> int:
    # Get the length of the input nums array
    n_len = len(nums)
    # Initialize a dp array with all elements set to 1 to represent the length of the LIS ending at each index
    dp = [1 for _ in range(len(nums))]

    # Iterate over each index of the nums array
    for idx in range(1, len(nums)):
      # Iterate over previous indices
      for idx2 in range(idx):
        # If nums[idx2] is less than nums[idx], it means nums[idx] can be included in the LIS
        if nums[idx2] < nums[idx]:
          # Update the value of dp[idx] to represent the length of the LIS ending at index idx
          dp[idx] = max(dp[idx], dp[idx2] + 1)
    # Return the maximum value in the dp array, which represents the length of the LIS
    return max(dp)
