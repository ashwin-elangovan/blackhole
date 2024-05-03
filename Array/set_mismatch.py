class Solution:

  def findErrorNums(self, nums: List[int]) -> List[int]:
    # Initialize an empty set to store unique numbers
    num_set = set()
    # Get the length of the input list
    nums_len = len(nums)
    # Calculate the expected sum of numbers from 1 to n using the formula n * (n + 1) / 2
    expected_sum = (nums_len * (nums_len + 1)) // 2
    # Calculate the current sum of the numbers in the input list
    current_sum = sum(nums)

    # Iterate over the indices and elements of the input list
    for idx, num in enumerate(nums):
      # If the current number is already in the set, it's the duplicate number
      if num in num_set:
        # Return the duplicate number and the missing number
        return [num, expected_sum - (current_sum - num)]
      # Add the current number to the set
      num_set.add(num)

    # If no duplicate is found, return -1 (not used in this context)
    return -1
