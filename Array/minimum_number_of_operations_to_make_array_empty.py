class Solution:

  def minimumRounds(self, tasks: List[int]) -> int:
    # Count the occurrences of each task
    ctr = Counter(tasks)
    # Initialize the final count
    final_count = 0
    # Iterate over the task counts
    for key, value in ctr.items():
      # If a task occurs less than twice, it's not possible to form a group
      if value < 2:
        return -1
      # Calculate the number of rounds needed for each task group
      final_count += (value // 3)
      # If there are remaining tasks after forming groups of 3, an additional round is needed
      if value % 3:
        final_count += 1
    # Return the final count of rounds needed
    return final_count
