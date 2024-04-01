class Solution:

  def maximumOddBinaryNumber(self, s: str) -> str:
    count_value = Counter(s)
    # Order is max 1's should be in the front and only one 1 should be at the last
    return '1' * (count_value['1'] - 1) + '0' * (count_value['0']) + '1'
