class Solution:

  def partitionString(self, s: str) -> int:
    # Initialize a variable to represent the bitmask
    flag = 0
    # Initialize a variable to count the number of substrings
    substr_count = 0

    # Iterate through each character in the string
    for ch in s:
      # Calculate the value of the current character using ASCII values
      val = ord(ch) - ord('a')

      # Check if the current character has already appeared in the current substring
      if flag & (1 << val):
        # If yes, increment the substring count and reset the flag
        substr_count += 1
        flag = 0

      # Update the flag by setting the bit corresponding to the current character
      flag |= (1 << val)

    # Increment the substring count by 1 to account for the last substring
    return substr_count + 1
