class Solution:

  def missingNumber(self, nums: List[int]) -> int:
    # Initialize the result variable to store the missing number.
    result = 0

    # Iterate through the indices and values of nums.
    for idx, value in enumerate(nums):
      # XOR operation with index + 1 to include the possibility of nums being 0-indexed.
      result ^= idx + 1
      # XOR operation with the value from nums.
      result ^= value

    # At the end, result will hold the missing number.
    return result
