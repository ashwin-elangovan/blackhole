from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        ctr = Counter(nums)

        # Initialize a bucket array to store numbers by their frequency
        bucket_arr = [[] for _ in range(len(nums)+1)]

        # Place numbers in the bucket array based on their frequency
        for key, count in ctr.items():
            bucket_arr[count].append(key)

        # Initialize the final array to store the top k frequent numbers
        final_arr = []

        # Traverse the bucket array from right to left
        for idx in range(len(bucket_arr)-1, 0, -1):
            # If the bucket is not empty and there are still elements needed to fulfill k
            if len(bucket_arr[idx]) != 0 and k > 0:
                # Append numbers from the current bucket to the final array
                final_arr += bucket_arr[idx][:k]
                # Update the remaining count of elements needed
                k -= len(bucket_arr[idx])

        return final_arr
