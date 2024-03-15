# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"


class Solution:

  def reverseWords(self, s: str) -> str:
    return " ".join(reversed(s.split()))


class Solution:

  def reverseWords(self, s: str) -> str:
    words_arr = []  # List to store individual words
    temp_str = ""  # Temporary string to build each word

    # Iterate through each character in the input string
    for char in s:
      if char != " ":
        temp_str += char  # Append non-space characters to temporary string
      elif temp_str != "":
        words_arr.append(temp_str)  # Add completed word to the list
        temp_str = ""  # Reset temporary string for next word

    # Check if there's any remaining word in the temporary string
    if temp_str != '':
      words_arr.append(temp_str)

    # Join the words in reverse order with spaces in between
    return " ".join(words_arr[::-1])
