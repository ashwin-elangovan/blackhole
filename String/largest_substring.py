# Given a string s, find the longest subtring of str and return an array of length 2, such that the 0th index must contain the starting index of the largest substring and the 1st index must contain the length of the largest substring.

# Constraints:
# 0 <= str.length <= 10000
# s can contain any character

# Example:
# Input: str = "aaBBccccc"
# Output: {4, 5}
# Explanation: ccccc is the largest substring in str with starting index of 4 and length of 5.

# Input: str = "122201111133"
# Output: {5, 5}


def largest_substring(string):
  max_len = 0
  max_char = ''
  first_occurence = {}
  curr_len = 0
  curr_char = ''
  # start_idx = 0

  for i in range(len(string)):
    if string[i] == curr_char:
      curr_len += 1
      if curr_len > max_len:
        max_len = curr_len
        max_char = string[i]
    else:
      curr_char = string[i]
      curr_len = 1
      first_occurence[curr_char] = i
  return [first_occurence[max_char], max_len]


print(largest_substring("aaBBccccc"))
print(largest_substring("122201111133"))
