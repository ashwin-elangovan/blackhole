# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # Initialize an empty stack to simulate the state of asteroids

        for a in asteroids:
            # Check for collisions between asteroids moving in opposite directions 
            # Last element of stack moves right and current element in loop moves left
            while stack and stack[-1] >= 0 and a < 0:
                # Calculate the collision result between the last element in the stack and the current element
                collision = stack[-1] + a

                # If the collision result is non-positive, the last element in the stack is destroyed
                if collision <= 0:
                    stack.pop()

                # If the collision result is non-negative, the new asteroid (current element) is destroyed,
                # or both the current asteroid and the last element are destroyed
                if collision >= 0:
                    break

            else:
                # If no collision occurs, or the current asteroid survives a collision, add it to the stack
                stack.append(a)
        
        return stack  # Return the updated state of asteroids after all collisions
