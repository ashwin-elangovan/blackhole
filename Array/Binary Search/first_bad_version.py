class Solution:

def firstBadVersion(self, n) -> int:
    # Initialize left and right pointers to represent the range of versions
    left, right = 1, n

    # Binary search loop to find the first bad version
    while left < right:
        # Calculate the midpoint of the current range
        mid = left + (right - left) // 2

        # Check if the midpoint version is a bad version
        if isBadVersion(mid):
            # If it's bad, update the right pointer to search in the left half
            right = mid
        else:
            # If it's not bad, update the left pointer to search in the right half
            left = mid + 1

    # At this point, left and right pointers converge to the first bad version
    return left
