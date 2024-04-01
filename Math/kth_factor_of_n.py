from math import sqrt


class Solution:

  def kthFactor(self, n: int, k: int) -> int:
    # Initialize two lists to store factors
    factor1 = []  # Store factors from 1 to sqrt(n)
    factor2 = []  # Store factors from sqrt(n) to n

    # Iterate through numbers from 1 to sqrt(n)
    for number in range(1, int(sqrt(n)) + 1):
      # Check if the current number is a factor of n
      if n % number == 0:
        factor1.append(number)  # Add the factor to factor1
        factor2.append(n // number)  # Add the corresponding factor to factor2

    # Check if the last factor in factor1 and factor2 is the same
    if factor1[-1] == factor2[-1]:
      factor2.pop()  # Remove the duplicate factor from factor2

    # Concatenate factor1 and reverse of factor2 to get all factors in ascending order
    factors = factor1 + factor2[::-1]

    # Check if k is within the range of factors
    return -1 if len(factors) < k else factors[
      k - 1]  # Return the kth factor or -1 if k is out of range
