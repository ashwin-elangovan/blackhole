class Solution:

  def sortEvenOdd(self, nums: List[int]) -> List[int]:
    # Initialize lists to store even and odd elements
    odd = []
    even = []

    # Iterate through the input list
    for idx, value in enumerate(nums):
      # Check if the index is even or odd
      if idx % 2 == 0:
        even.append(value)  # Append even-indexed elements to the even list
      else:
        odd.append(value)  # Append odd-indexed elements to the odd list

    # Sort the odd list in descending order
    odd.sort(reverse=True)
    # Sort the even list in ascending order
    even.sort()

    # Initialize indices for even and odd lists
    o_idx = 0
    e_idx = 0

    # Initialize the final array to store sorted even and odd elements
    final_arr = []

    # Merge elements from even and odd lists into the final array
    while e_idx < len(even) or o_idx < len(odd):
      # Append even element if there are elements left in the even list
      if e_idx < len(even):
        final_arr.append(even[e_idx])
        e_idx += 1

      # Append odd element if there are elements left in the odd list
      if o_idx < len(odd):
        final_arr.append(odd[o_idx])
        o_idx += 1

    return final_arr
