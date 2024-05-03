class Solution:

  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # Initialize pointers for iterating over nums1, nums2, and the merged list
    i = m - 1
    j = n - 1
    k = m + n - 1

    # Iterate over nums1 and nums2 from the end and merge them into nums1
    while j >= 0:
      # If there are elements remaining in nums1 and nums1[i] is greater than nums2[j]
      if i >= 0 and nums1[i] > nums2[j]:
        # Move the greater element from nums1 to the end of nums1
        nums1[k] = nums1[i]
        i -= 1
      else:
        # Move the current element from nums2 to the end of nums1
        nums1[k] = nums2[j]
        j -= 1

      # Move the pointer for the merged list to the previous position
      k -= 1

    # Return the merged nums1 list
    return nums1
