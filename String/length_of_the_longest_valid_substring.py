class Solution(object):

  def longestValidSubstring(self, word, forbidden):
    # Convert the list of forbidden words to a set for faster lookup
    forbidden = set(forbidden)

    # Initialize variables to keep track of the left boundary of the current substring
    left = 0
    # Initialize the length of the longest valid substring found so far
    res_len = 0

    # Loop through each character index in the word
    for idx in range(len(word)):
      # Move a pointer backwards from the current index to check substrings
      # The range ensures that the pointer does not go beyond 10 characters to the left
      # Forbidden strings have a max len of 10
      for mov_ptr in range(max(idx - 10, left), idx + 1):
        # Check if the substring from the moving pointer to the current index is forbidden
        if word[mov_ptr:idx + 1] in forbidden:
          # If forbidden, update the left boundary to be one character ahead of the moving pointer
          left = mov_ptr + 1
      # Update the length of the longest valid substring found so far
      res_len = max(res_len, idx - left + 1)

    # Return the length of the longest valid substring
    return res_len
