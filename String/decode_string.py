class Solution:

  def decodeString(self, s: str) -> str:
    stack = []  # Initialize an empty stack to store characters

    for char in s:  # Iterate through each character in the input string 's'
      if char != ']':  # If the current character is not ']'
        stack.append(char)  # Push it onto the stack
      else:  # If the current character is ']'
        substr = ''  # Initialize an empty string to store the substring
        while stack[
            -1] != '[':  # Pop characters from the stack until '[' is encountered
          substr = stack.pop(
          ) + substr  # Concatenate characters to form the substring
        stack.pop()  # Pop '[' from the stack (to discard it)

        curr_num = ''  # Initialize an empty string to store the repetition count
        while stack and stack[-1].isdigit(
        ):  # Pop digits from the stack to form the repetition count
          curr_num = stack.pop(
          ) + curr_num  # Concatenate digits to form the number

        # Multiply the substring by the repetition count and push the result back onto the stack
        stack.append(int(curr_num) * substr)

    # Concatenate all elements from the stack to form the final decoded string
    return ''.join(stack)
