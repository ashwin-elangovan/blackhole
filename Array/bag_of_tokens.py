class Solution:
  def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
      # Initialize two pointers, left and right, at the beginning and end of the sorted tokens list respectively.
      left, right = 0, len(tokens)-1

      # Sort the tokens list in non-decreasing order. This allows efficient token selection.
      tokens.sort()

      # Initialize variables to keep track of the current score and the maximum score obtained.
      score = 0
      max_score = 0

      # Continue the loop until the left pointer surpasses the right pointer.
      while left <= right:
          # If the current token at the left pointer can be bought with the available power,
          # then buy the token, increase the score, and move the left pointer to the next token.
          if tokens[left] <= power:
              power -= tokens[left]
              score += 1
              left += 1

              # Update the maximum score obtained so far if the current score exceeds it.
              max_score = max(max_score, score)

          # If it's not possible to buy more tokens but we have some tokens to spend (score > 0),
          # then trade the token with the highest value (at right pointer) for power.
          elif score > 0:
              power += tokens[right]
              score -= 1
              right -= 1

          # If we cannot buy more tokens and cannot trade either, break the loop.
          else:
              break

      # Return the maximum score obtained.
      return max_score
