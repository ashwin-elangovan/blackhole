from collections import Counter
from typing import List


class Solution:

  def maxFrequencyElements(self, nums: List[int]) -> int:
    # Count the frequency of each element in nums
    ctr = Counter(nums)

    # Find the maximum frequency among all elements
    max_value = max(ctr.values())

    # Sum up the frequencies of elements that have the maximum frequency
    final_val = sum(value for key, value in ctr.items() if value == max_value)

    # Return the total frequency of elements with the maximum frequency
    return final_val
