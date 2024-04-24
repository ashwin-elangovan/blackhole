class Solution:

  def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    # Initialize a variable to store the total time required
    count = 0

    # Iterate through the list of tickets
    for idx in range(len(tickets)):
      # Check if the current ticket index is less than or equal to the chosen ticket index
      if idx <= k:
        # If it is, add the minimum of the tickets at the current index and the chosen index to the total count
        count += min(tickets[idx], tickets[k])
      else:
        # If it's not, subtract 1 from the ticket count at the chosen index and add the minimum to the total count
        count += min(tickets[idx], tickets[k] - 1)

    # Return the total time required
    return count
