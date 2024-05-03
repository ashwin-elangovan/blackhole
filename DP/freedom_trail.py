class Solution:

  def findRotateSteps(self, ring: str, key: str) -> int:
    # Initialize an array to store the minimum steps needed to align each character in the ring with the current character in the key
    dp = [0] * len(ring)

    # Iterate over the characters in the key in reverse order
    for k in reversed(range(len(key))):
      # Initialize a temporary array to store the minimum steps needed for the current character alignment
      curr_dp = [float('inf')] * len(ring)

      # Iterate over each character position in the ring
      for r in range(len(ring)):
        # Check if the current character in the ring matches the current character in the key
        for idx, c in enumerate(ring):
          if key[k] == c:
            # Calculate the minimum cost to rotate the ring to align the characters
            min_cost = min(abs(r - idx), len(ring) - abs(r - idx))
            # Update the minimum steps needed for the current character alignment
            curr_dp[r] = min(curr_dp[r], dp[idx] + 1 + min_cost)

      # Update the dp array with the minimum steps needed for the current character alignment
      dp = curr_dp

    # Return the minimum steps needed to align the first character in the ring with the first character in the key
    return dp[0]
