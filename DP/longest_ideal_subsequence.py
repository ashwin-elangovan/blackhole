class Solution:

  def longestIdealString(self, s: str, k: int) -> int:
    # Initialize an array to store the longest ideal string length for each character
    dp = [0 for _ in range(26)]

    # Iterate through each character in the input string
    for idx in range(len(s)):
      # Convert the character to its corresponding index in the range [0, 25]
      i = ord(s[idx]) - ord('a')

      # Initialize the longest ideal string length for the current character
      longest = 1

      # Iterate through all characters in the alphabet
      for j in range(26):
        # Check if the absolute difference between the indices is less than or equal to k
        if abs(i - j) <= k:
          # Update the longest ideal string length if the condition is met
          longest = max(longest, dp[j] + 1)

      # Update the longest ideal string length for the current character in the dp array
      dp[i] = max(longest, dp[i])

    # Return the maximum value in the dp array, which represents the maximum length of the ideal string
    return max(dp)
