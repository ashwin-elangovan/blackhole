class Solution:
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
      # Convert the list of words into a set for efficient lookup
      wordList = set(words)

      # Dictionary to store the results of subproblems
      dp = {}

      # Depth-first search (DFS) function to check if a word can be concatenated
      def dfs(word):
          # Base case: if the word is empty, return False
          if not word:
              return False

          # If the word has already been processed, return its result from dp
          if word in dp:
              return dp[word]

          # Iterate through all possible partitions of the word
          for idx in range(len(word)):
              # Check if both left and right substrings are in the wordList
              if (word[:idx] in wordList and word[idx:] in wordList) or \
                      # Or if left substring is in wordList and right substring can be concatenated
                      (word[:idx] in wordList and dfs(word[idx:])):
                  # Mark the word as concatenated and return True
                  dp[word] = True
                  return dp[word]

          # If no valid concatenation is found, mark the word as not concatenated and return False
          dp[word] = False
          return dp[word]

      # List to store the final concatenated words
      final_arr = []

      # Iterate through each word in the input list
      for word in words:
          # Check if the word can be concatenated using the DFS function
          if dfs(word):
              # If yes, add it to the final concatenated words list
              final_arr.append(word)

      # Return the list of concatenated words
      return final_arr
