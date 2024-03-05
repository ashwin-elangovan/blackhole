class Solution:
  def minimumLength(self, s: str) -> int:
      # Calculate the length of the input string
      str_len = len(s)

      # Initialize two pointers 'left' and 'right' to the start and end of the string respectively
      left, right = 0, len(s) - 1

      # Iterate until the 'left' pointer is less than the 'right' pointer
      while left < right:
          # If the characters at the 'left' and 'right' pointers are equal
          if s[left] == s[right]:
              # Store the current character value
              curr_val = s[left]

              # Move the 'left' pointer until it reaches a different character than 'curr_val'
              while left <= right and s[left] == curr_val:
                  left += 1

              # Move the 'right' pointer until it reaches a different character than 'curr_val'
              while left <= right and s[right] == curr_val:
                  right -= 1
          else:
              # Break the loop if the characters at 'left' and 'right' are different
              break

      # Return the length of the remaining substring
      return len(s[left:right+1])
