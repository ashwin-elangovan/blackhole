class Solution:

  def pivotInteger(self, n: int) -> int:
    # rev_sum = 0
    # for num in range(n, -1, -1):
    #     rev_sum += num
    #     if rev_sum == ((num)*(num+1))/2:
    #         return num
    # return -1
    sum_val = n * (n + 1) // 2
    root_val = sqrt(sum_val)
    return -1 if root_val % 1 else int(root_val)
