# As the ruler of a kingdom, you have an army of wizards at your command.

# You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:

# The strength of the weakest wizard in the group.
# The total of all the individual strengths of the wizards in the group.
# Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 109 + 7.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Think of the stack as a "waiting list" of wizards. We keep adding wizards to the stack until we find a weaker wizard. When we find a weaker wizard, we calculate the total strength of the subarray ending at that wizard and add it to the answer. We repeat this process until we have processed all wizards.
# The prefix sum array helps us efficiently calculate the sum of strengths in each subarray. The stack helps us efficiently find the nearest smaller value to the left of each element, which is essential for finding the subarrays.

# As we iterate through the strengths, we compare the current strength with the strength on top of the stack.
# If the current strength is less than or equal to the strength on top of the stack, it means we've found a range where the strengths are decreasing or staying the same.
# We pop elements from the stack until we find a strength that is greater than the current strength. For each popped element, we calculate its contribution to the total strength based on the range it covers and its strength value.
# We add up these contributions to get the total strength.


# https://leetcode.com/problems/sum-of-total-strength-of-wizards/solutions/2063910/python-3-prefix-sum-graphically-explained/


# This is a class definition for the Solution class
class Solution:

    # This is the function definition for the totalStrength function
    # It takes a list of integers called strength as input
    # The function returns an integer, which is the total strength
    # This function is used to calculate the total strength based on the given strength list
    def totalStrength(self, strength: List[int]) -> int:

        # Initialize the answer variable to 0
        # This variable will store the final total strength
        # We start with 0 and accumulate the contributions to the total strength
        ans = 0

        # Initialize an empty list called stack
        # This list will be used as a stack data structure
        # to keep track of the indices and values of the strength list
        # We use a stack to efficiently find the nearest smaller value to the left of each element
        stack = []

        # Create a prefix sum list called prefix
        # This list will store the prefix sum of the prefix sum of the strength list
        # The first accumulate operation computes the prefix sum of the strength list
        # The second accumulate operation computes the prefix sum of the result of the first accumulate
        # The initial value of the second accumulate function is set to 0
        # This double prefix sum allows efficient calculation of the sum of elements between any two indices
        # We need this to calculate the contribution of each element to the total strength
        prefix = list(accumulate(accumulate(strength), initial=0))

        # Iterate over the strength list and an additional 0 at the end
        # The enumerate function is used to get both the index and value of each element
        # We iterate over the strength list and an additional 0 to handle the case where the last element is the maximum
        for i, x in enumerate(strength + [0]):

            # While the stack is not empty and the top element of the stack
            # has a value greater than or equal to the current value x
            # We find the nearest smaller value to the left of the current element
            while stack and stack[-1][1] > x:
                # Here, mid is the index of the current element, lo is the index of the nearest smaller element to the left of mid, right is the sum of elements to the right of mid, and left is the sum of elements to the left of mid.

                # Pop the top element from the stack
                # and store its index in the mid variable
                # This is the index of the nearest smaller value to the left of the current element
                mid = stack.pop()[0]

                # If the stack is not empty, get the index of the second top element
                # Otherwise, set lo to -1
                # This is the index of the next smaller value to the left of mid
                lo = stack[-1][0] if stack else -1

                # Calculate the sum of elements to the left of mid
                # from the prefix sum list
                # This is done by subtracting the prefix sum at lo from the prefix sum at mid
                # If lo is -1, the prefix sum at 0 is used, which is 0
                # We need this to calculate the contribution of the mid element to the total strength
                left = prefix[mid] - prefix[max(lo, 0)]

                # Calculate the sum of elements to the right of mid
                # from the prefix sum list
                # This is done by subtracting the prefix sum at mid from the prefix sum at i
                # We need this to calculate the contribution of the mid element to the total strength
                right = prefix[i] - prefix[mid]

                # The formula calculates the contribution by considering the strength value of the element, the number of smaller elements to the left (mid - lo), and the number of smaller elements to the right (i - mid), multiplied by the sum of elements to the left and right.

                # Update the answer by adding the contribution of the current mid value
                # The contribution is calculated as:
                # strength[mid] * (right * (mid - lo) - left * (i - mid))
                # This formula calculates the total strength contribution of the mid element
                # based on the strength value and the sum of elements to the left and right
                # The modulo operation is used to keep the answer within the range of the given modulus
                ans += (strength[mid] * (right * (mid - lo) - left * (i - mid))) % 1_000_000_007

            # Push the current index and value onto the stack
            # We add the current index and value to the stack to find the nearest smaller value for the next element
            stack.append((i, x))

        # Return the final answer
        # After iterating over all elements and accumulating their contributions, we return the final total strength
        return ans