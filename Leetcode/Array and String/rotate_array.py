# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Let k=3.

# Original List                   : 1 2 3 4 5 6 7
# After reversing all numbers     : 7 6 5 4 3 2 1
# After reversing first k numbers : 5 6 7 4 3 2 1
# After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums) # K can be any number. If k is greater than array length, this will take care and reduce the required rotates
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1


Brute force approach:

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # speed up the rotation
        k %= len(nums) # Taking care of array length

def reverse(nums, k):
    for i in range(k):
        last = nums[-1] # last number
        for j in range(len(nums)):
            nums[j], last = last, nums[j]


        