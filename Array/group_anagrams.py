from collections import defaultdict


class Solution:

  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # Dictionary to store anagrams grouped by their character counts
    final_hash = defaultdict(list)

    # Iterate through each string in the input list
    for string in strs:
      # Array to store the count of each character in the current string
      arr = [0] * 26

      # Count the occurrences of each character in the string
      for ch in string:
        num_val = ord(ch) - ord('a')  # Convert character to numeric value
        arr[num_val] += 1

      # Convert the array into a tuple to use as a key in the dictionary
      # Add the current string to the list of anagrams with the same character count
      final_hash[tuple(arr)].append(string)

    # Return the values of the dictionary, which are lists of grouped anagrams
    return final_hash.values()
