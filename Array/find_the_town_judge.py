from collections import defaultdict
from typing import List


class Solution:

  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    # If there are no trust relations and only one person, that person is considered the judge
    if len(trust) == 0 and n <= 1:
      return 1

    # Initialize a defaultdict to store the count of trusts for each person
    # Initialize the count for each person as 0
    count_hash = defaultdict(lambda: 0)

    # Iterate over each trust relationship
    for trusting, trusted in trust:
      # Increment the count of trusts for the trusted person
      if count_hash[trusted] != -1:
        count_hash[trusted] += 1

      # Mark the trusting person as ineligible to be the judge
      count_hash[trusting] = -1

    # Iterate over the count of trusts for each person
    for key, value in count_hash.items():
      # If a person has been trusted by all others (except themselves), they are the judge
      if value == n - 1:
        return key

    # If no judge is found, return -1
    return -1
