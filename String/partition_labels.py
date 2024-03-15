class Solution:
  def partitionLabels(self, s: str) -> List[int]:
      # Create a dictionary to store the last occurrence index of each character
      char_dict = {}
      for idx, ch in enumerate(s):
          char_dict[ch] = idx

      count = 0  # Counter to keep track of the current partition length
      partition = []  # List to store the lengths of partitions
      max_end = 0  # Variable to keep track of the maximum end index of the current partition

      # Iterate over the string
      for idx, ch in enumerate(s):
          # Update the maximum end index of the current partition
          max_end = max(max_end, char_dict[ch])

          # Increment the counter for the current partition
          count += 1

          # If the current index reaches the maximum end index of the current partition,
          # it indicates the end of the current partition
          if idx == max_end:
              partition.append(count)  # Append the length of the current partition to the partition list
              count = 0  # Reset the counter for the next partition

      return partition  # Return the list of partition lengths
