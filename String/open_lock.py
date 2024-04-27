class Solution(object):

  def openLock(self, deadends, target):
    # Initialize a queue with the starting point '0000'
    queue = deque(['0000'])
    # Convert the deadends list to a set for faster lookup
    visited = set(deadends)
    # Initialize the final count to -1
    final_count = -1

    # Perform BFS traversal
    while queue:
      # Increment the final count for each level of traversal
      final_count += 1

      # Iterate through the current level of the queue
      for _ in range(len(queue)):
        # Pop the current value from the left of the queue
        curr_value = queue.popleft()

        # Check if the current value matches the target
        if curr_value == target:
          # Return the final count if the target is found
          return final_count

        # Skip the current value if it's in the set of deadends
        if curr_value in visited:
          continue

        # Add the current value to the set of visited nodes
        visited.add(curr_value)

        # Generate the next possible combinations by incrementing or decrementing each digit
        for i, ch in enumerate(curr_value):
          num = int(ch)
          # Append the new combination to the queue
          queue.append(curr_value[:i] + str((num - 1) % 10) +
                       curr_value[i + 1:])
          queue.append(curr_value[:i] + str((num + 1) % 10) +
                       curr_value[i + 1:])

    # Return -1 if the target is not reachable
    return -1
