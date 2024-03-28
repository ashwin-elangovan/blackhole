class Solution:

  def findMaxLength(self, nums: List[int]) -> int:
    # Initialize a dictionary to store the running sum and its corresponding index
    # Initialize it with 0 at index -1 to handle cases where the running sum becomes 0
    sum_hash = {0: -1}

    # Initialize variables to keep track of the running count, maximum length, and current index
    count = 0
    max_len = 0

    # Iterate through the array
    for idx, num in enumerate(nums):
      # Update the running count based on the current number
      if num == 0:
        count -= 1
      else:
        count += 1

      # Check if the current running count exists in the sum_hash
      if count in sum_hash:
        # If it exists, update the maximum length if the current subarray length is greater
        max_len = max(max_len, idx - sum_hash[count])
      else:
        # If it doesn't exist, add the current running count to the sum_hash with its index
        sum_hash[count] = idx

    # Return the maximum length found
    return max_len
