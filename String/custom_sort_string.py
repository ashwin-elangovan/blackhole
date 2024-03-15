class Solution:

  def customSortString(self, order: str, s: str) -> str:
    # Create a counter dictionary to store the frequency of characters in string s
    count_dict = Counter(s)

    # Initialize an empty string to store the final sorted string
    final_str = ""

    # Iterate through each character in the custom order
    for char in order:
      # If the character exists in the counter dictionary
      if char in count_dict:
        # Append the character to the final string according to its frequency
        final_str += char * count_dict[char]
        # Remove the character from the dictionary
        count_dict.pop(char)

    # Append any remaining characters in s that are not in the custom order to the final string
    for key, value in count_dict.items():
      final_str += key * value

    # Return the final sorted string
    return final_str
