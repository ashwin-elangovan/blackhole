
# 26. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Brute force in ruby
# def remove_duplicates(nums)
#     size = nums.length
#     h = {}
#     nums.each do |val|
#         h[val] = 1
#     end
#     k_size = h.keys.length
#     nums = h.keys
#     n_size = size - k_size
#     n_size.times do
#         nums << "-"
#     end
#     nums
# end

# Optimized ruby

# def remove_duplicates(nums)
#   return 0 if nums.length.zero?
#   i = 0
#   for j in 1..(nums.length-1) do
#     if nums[j] > nums[i]
#       i+=1
#       nums[i] = nums[j]
#     end
#   end
#   i+1
# end


class Solution:
  def removeDuplicates(nums):
      i = 0
      for j in range(1,len(nums)):
          if nums[j] > nums[i]:
              i += 1
              nums[i] = nums[j]
      return i+1
# OR

class Solution(object):
  def removeDuplicates(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      nums[:] = sorted(list(set(nums))) # nums[:] will change the original array instead of creating a new variable nums
      return len(nums)