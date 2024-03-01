from typing import List

class Solution:
    def maxCrossingSum(self, nums: List[int], l: int, m: int, h: int) -> int:
        sm = 0
        left_sum = float('-inf')

        for i in range(m, l-1, -1):
            sm += nums[i]
            left_sum = max(left_sum, sm)

        sm = 0
        right_sum = float('-inf')
        for i in range(m, h + 1):
            sm += nums[i]
            right_sum = max(right_sum, sm)

        return max(left_sum + right_sum - nums[m], left_sum, right_sum)

    def maxSubArraySum(self, nums: List[int], l: int, h: int) -> int:
        if l > h:
            return float('-inf')

        if l == h:
            return nums[l]

        m = (l + h) // 2

        return max(
            self.maxSubArraySum(nums, l, m-1),
            self.maxSubArraySum(nums, m+1, h),
            self.maxCrossingSum(nums, l, m, h)
        )

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = self.maxSubArraySum(nums, 0, n-1)
        return max_sum

# Example Usage:
# arr = [2, 3, 4, 5, 7]
# solution = Solution()
# max_sum = solution.maxSubArray(arr)
# print("Maximum contiguous sum is", max_sum)