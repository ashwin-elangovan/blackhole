class Solution:

  def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0: return False
    # 7->0000 0111
    # 8->0000 1000
    return n & n - 1 == 0
