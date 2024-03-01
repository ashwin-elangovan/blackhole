# Pascal's Triangle Generation

# You are given a non-negative integer n. Generate the first n rows of Pascal's Triangle.

# Pascal's Triangle is a mathematical concept where each number is the sum of the two numbers directly above it.

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1]*i for i in range(1, n+1)] # initialize triangle with all 1
        for i in range(1, n): # 2nd row to last row
            for j in range(1, i): # 2nd element to 2nd last element
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1] # update each as sum of two elements from above row
        return ans
        