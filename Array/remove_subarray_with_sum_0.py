def update_array(arr):
  # If the input array is empty, return an empty list
  if not arr:
      return []

  # Create a dictionary to store the prefix sum and its index
  prefix_sum = defaultdict(lambda: 0)
  curr_sum = 0
  # Iterate through the array to calculate the prefix sum and store it in the dictionary
  for idx, num in enumerate(arr):
      curr_sum += num
      prefix_sum[curr_sum] = idx

  # Reset current sum and initialize index
  curr_sum = 0
  idx = 0
  # Iterate through the array
  while idx < len(arr):
      # Update current sum
      curr_sum += arr[idx]
      # If the current sum is zero, replace the subarray from the beginning up to the current index with 'x'
      if curr_sum == 0:
          arr[:idx+1] = 'x' * (idx+1)
          idx += 1
      # If the current sum is found in the prefix sum dictionary and the index is not equal to the current index,
      # replace the subarray from the next index after the current index up to the index stored in the dictionary with 'x'
      elif prefix_sum[curr_sum] != idx:
          arr[idx+1:prefix_sum[curr_sum]+1] = 'x' * (prefix_sum[curr_sum]-idx)
          idx = prefix_sum[curr_sum]+1
      # If the current sum is not found in the prefix sum dictionary or the index is equal to the current index, 
      # move to the next index
      else:
          idx += 1
  # Return the updated array with 'x' replaced subarrays removed
  return [x for x in arr if x != 'x']
