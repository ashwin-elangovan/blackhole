from typing import List
from collections import defaultdict, Counter

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Create a defaultdict to store website mappings for each user
        user_mappings = defaultdict(list)

        # Sort the data by timestamp and populate the user mappings
        for u, t, w in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            user_mappings[u].append(w)

        # Initialize a Counter to count the occurrence of sequences
        counter = Counter()

        # Iterate through each user's website mappings
        for user, mappings in user_mappings.items():
            s = set()  # Initialize a set to store unique sequences of length 3
            mappings_len = len(mappings)

            # for triple_set in set(itertools.combinations(mappings, 3)):
            #     counter[triple_set] += 1

            # Iterate through all possible combinations of 3 websites
            if mappings_len >= 3:
                for i in range(mappings_len-2):
                    for j in range(i+1, mappings_len-1):
                        for k in range(j+1, mappings_len):
                            s.add((mappings[i], mappings[j], mappings[k]))

                # Increment the count for each unique sequence
                for t in s:
                    counter[t] += 1

        # Find the most visited sequence based on count and lexicographical order
        final_val = sorted(counter.items(), key= lambda x: (-x[1], x[0]))[0][0]
        return list(final_val)  # Return the most visited sequence as a list
