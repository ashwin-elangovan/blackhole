from collections import Counter


class Solution:

  def minimumKeypresses(self, s: str) -> int:
    # Count the frequency of each character in the input string
    ctr = Counter(s)

    # Sort the characters based on their frequencies in descending order
    ctr = sorted(ctr.items(), key=lambda x: -x[1])

    final = 0  # Initialize the total number of key presses

    # Iterate through the sorted characters
    for idx, item in enumerate(ctr):
      # Calculate the level of the character based on its index
      level = (idx // 9) + 1

      # Add the number of key presses required for this character at its level
      final += item[1] * level

    return final  # Return the total number of key presses
