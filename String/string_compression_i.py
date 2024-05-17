# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.


class Solution:

    def compress(self, chars: List[str]) -> int:
        # Initialize pointers and count
        read_ptr = write_ptr = 0
        count = 1

        # Helper function to write compressed representation to chars
        def write_compressed(char, count):
            nonlocal write_ptr
            chars[write_ptr] = char
            write_ptr += 1
            if count > 1:
                for digit in str(count):
                    chars[write_ptr] = digit
                    write_ptr += 1

        # Iterate through the input array
        for read_ptr in range(len(chars)):
            # If it's the last character or different from the next one
            if read_ptr == len(chars) - 1 or chars[read_ptr] != chars[read_ptr
                                                                      + 1]:
                write_compressed(chars[read_ptr], count)
                count = 1
            else:
                # If it's the same as the next character, increment count
                count += 1

        return write_ptr  # Return the length of the compressed array
