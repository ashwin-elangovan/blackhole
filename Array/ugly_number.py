class Solution:

  def isUgly(self, n: int) -> bool:
    # If the number is non-positive, it cannot be ugly
    if n <= 0:
      return False

    # Check divisibility by 2, 3, and 5
    for divisor in [2, 3, 5]:
      # While n is divisible by the current divisor, keep dividing
      while n % divisor == 0:
        n //= divisor

    # If after division n becomes 1, it means n only has factors 2, 3, and 5
    return n == 1
