class Solution:

  def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    # Sort the deck in descending order
    deck = sorted(deck, reverse=True)

    # Initialize a deque to store the final arrangement
    final_q = deque()

    # Iterate through the sorted deck
    for card in deck:
      # If the deque is not empty, pop the last element and append it to the front
      if len(final_q) != 0:
        curr = deque.pop(final_q)
        final_q.appendleft(curr)
      # Append the current card to the front of the deque
      final_q.appendleft(card)

    # Convert the deque to a list and return
    return list(final_q)
