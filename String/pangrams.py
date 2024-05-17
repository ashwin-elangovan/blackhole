# Check if a string is a pangram and if not return the missing characters
class Solution:

    def checkIfPangram(self, sentence: str) -> bool:
        arr = [0] * 26
        count = 0
        for ch in sentence:
            current_idx = ord(ch) - ord('a') - 1
            if arr[current_idx] == 0:
                arr[current_idx] = 1
                count += 1
            if count == 26:
                return True

        missing_values = []
        for idx, value in enumerate(arr):
            if value == 0:
                curr_ascii = ord('a') + idx + 1
                missing_values.append(chr(curr_ascii))
        return missing_values


s = Solution()
print(s.checkIfPangram("thequickbrownfojumpsoverthelaydog"))
