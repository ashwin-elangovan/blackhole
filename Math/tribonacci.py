class Solution:

  def tribonacci(self, n: int) -> int:
    # Initialize the first three Tribonacci numbers
    t_0 = 0
    t_1 = 1
    t_2 = 1

    # Base cases: if n is 0, 1, or 2, return the corresponding Tribonacci number
    if n == 0:
      return t_0
    if n == 1:
      return t_1
    if n == 2:
      return t_2

    # Iteratively calculate Tribonacci numbers starting from the 3rd number
    for _ in range(n - 2):
      # Store the old value of t_2 for updating t_1
      t2_old = t_2

      # Update t_2 by adding the previous three Tribonacci numbers
      t_2 += t_0 + t_1

      # Update t_0 and t_1 for the next iteration
      t_0 = t_1
      t_1 = t2_old

    # Return the calculated Tribonacci number for n
    return t_2
