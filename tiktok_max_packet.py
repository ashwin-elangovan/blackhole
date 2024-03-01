def getMinimumDistortion(packets, max_frame):
  n = len(packets)
  max_diff = max(packets)  # Find the initial maximum absolute difference

  # Iterate through all possible values of x
  for x in range(max_frame + 1):
    new_packets = [x if packet == 0 else packet
                   for packet in packets]  # Apply the operation
    new_max_diff = max(abs(new_packets[i] - new_packets[i - 1]) for i in range(1, n))
    max_diff = min(max_diff, new_max_diff)  # Update the minimum distortion

  return max_diff



# Example usage:
n = 5
packets = [5, 0, 0, 0, 4]
max_frame = 10
result = getMinimumDistortion(packets, max_frame)
print(result)  # Output should be 2
