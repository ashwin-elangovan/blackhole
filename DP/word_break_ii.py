class Solution(object):
  def wordBreak(self, s, wordDict):
      # Convert wordDict to a set for faster lookup
      wordDict = set(wordDict)

      # Get the length of the input string
      str_len = len(s)

      # Initialize a list of lists to store possible sentences for each index of the string
      dp = [[] for _ in range(str_len+1)]

      # Initialize the list for the empty string as a list containing an empty string
      dp[0] = ['']

      # Iterate through each index of the string
      for idx in range(1, str_len+1):
          # Iterate through all possible prefixes of the current index
          for idx_2 in range(0, idx):
              # Check if the substring from a prefix to the current index is a valid word
              if dp[idx_2] and s[idx_2:idx] in wordDict:
                  # For each valid word, append it to all possible sentences ending at the current index
                  for sentence in dp[idx_2]:
                      if sentence:
                          dp[idx].append(sentence + " " + s[idx_2:idx])
                      else:
                          dp[idx].append(s[idx_2:idx])

      # Return the list of possible sentences ending at the last index of the string
      return dp[-1]
