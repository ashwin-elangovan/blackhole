class Solution(object):

  def wordBreak(self, s, wordDict):
    # Convert wordDict to set for efficient lookup
    wordDict = set(wordDict)

    # Initialize dynamic programming array with False
    dp = [False for _ in range(len(s) + 1)]

    # Base case: an empty string can be formed by word break
    dp[0] = True

    # Iterate through each index of the string
    for idx in range(1, len(s) + 1):
      # Iterate through each possible prefix ending at the current index
      for idx_2 in range(0, idx):
        # If the prefix is a valid word and the substring from idx_2 to idx is in wordDict
        if dp[idx_2] and s[idx_2:idx] in wordDict:
          # Update dp[idx] to True, indicating that a valid word break exists up to this index
          dp[idx] = True
          # Break the inner loop since we've found a valid word break for the current index
          break

    # Return whether a valid word break can be formed up to the last index of the string
    return dp[-1]
