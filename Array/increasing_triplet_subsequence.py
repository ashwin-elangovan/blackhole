class Solution:

  def increasingTriplet(self, nums: List[int]) -> bool:
    # Initialize two variables to store the smallest and second smallest elements
    first = second = float('inf')

    # Iterate through the numbers in the array
    for n in nums:
      # If the current number is less than or equal to the first, update the first
      if n <= first:
        first = n
      # If the current number is greater than the first but less than or equal to the second, update the second
      elif n <= second:
        second = n
      # If the current number is greater than both first and second, we have found a triplet
      else:
        return True

    # If no triplet is found after iterating through the array, return False
    return False
