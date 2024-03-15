class Solution:

  def distributeCandies(self, candyType: List[int]) -> int:
    # Calculate the maximum number of unique candy types that can be distributed
    # It is equal to the minimum of half of the total number of candies and the number of unique candy types
    return min(len(candyType) // 2, len(set(candyType)))
