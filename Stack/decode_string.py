  # Given an encoded string, return its decoded string.
  
  # The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
  
  # You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
  
  # The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

# When we hit an open bracket, we know we have parsed number for the contents of the bracket, so push (current_string, number) to the stack, so we can pop them on closing bracket to duplicate the enclosed string number times.

def decodeString(s: str):
    stack = []  # Initialize a stack to keep track of frames (current_string, k)
    current_string = ""  # Initialize an empty string to build the current string inside brackets
    k = 0  # Initialize k to keep track of the repetition count
    
    for char in s:
        if char == "[":
            # Push the current state (current_string, k) to the stack for the new frame
            stack.append((current_string, k))
            # Reset current_string and k for the new frame
            current_string = ""
            k = 0
        elif char == "]":
            # Pop the last state (last_string, last_k) from the stack
            last_string, last_k = stack.pop()
            # Update current_string by duplicating it using last_k
            current_string = last_string + last_k * current_string
        elif char.isdigit():
            # Update k by multiplying it by 10 and adding the current digit. Coz the numbers can be more than 1 digit. eg: 123[a]
            k = k * 10 + int(char)
        else:
            # Append the character to the current_string
            current_string += char
    
    return current_string

# This code iterates through the input string character by character. When it encounters an open bracket [, it saves the current state (current_string and k) onto the stack and resets them for the new frame. When it encounters a closing bracket ], it pops the last state from the stack, updates the current string by duplicating it using the last k, and continues. If the character is a digit, it updates the repetition count k. Otherwise, it appends the character to the current_string. Finally, it returns the decoded string.

