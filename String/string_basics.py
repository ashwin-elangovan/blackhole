
# Function to make the reverse of the string
def make_reverse(string: str) -> str:
    # Reversing the string
    string = string[::-1]
    # Splitting the string by space
    rev = string.split(" ")
    # Reversing the list of words
    rev = rev[::-1]
    # Joining the words to form a new string
    reversed_string = " ".join(rev)
    return reversed_string

# Driver code
if __name__ == "__main__":
    string = "Geeks for Geeks"
    print(make_reverse(string))

# This code is contributed by Shivam Tiwari

# Function to print all substrings
# Python program for the above approach
def printSubStrings(str):
	final_arr = []
	# First loop for starting index
	for i in range(len(str)):
		subStr = "";

		# Second loop is generating sub-String
		for j in range(i,len(str)):
			subStr += str[j];
			final_arr.append(subStr)
	print(final_arr)

# Driver Code
if __name__ == '__main__':
	str = "abcd";
	printSubStrings(str);

# This code is contributed by umadevi9616
