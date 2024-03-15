class Solution:

  def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    # new_set = set(nums1) & set(nums2)
    # if not new_set:
    #     return -1
    # return list(new_set)[0]

    len_1, len_2 = len(nums1), len(nums2)
    nums1_idx, nums2_idx = 0, 0

    while nums1_idx < len_1 and nums2_idx < len_2:
      if nums1[nums1_idx] == nums2[nums2_idx]:
        return nums1[nums1_idx]

      if nums1[nums1_idx] < nums2[nums2_idx]:
        nums1_idx += 1
      else:
        nums2_idx += 1
    return -1
