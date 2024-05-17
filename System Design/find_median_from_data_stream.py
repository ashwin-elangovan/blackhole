class MedianFinder:

    def __init__(self):
        # Initialize two heaps: small and large
        # small will store the smaller half of the numbers in max heap form
        # large will store the larger half of the numbers in min heap form
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Add the new number to the max heap (small)
        # '-num' is used because Python's heapq library provides a min heap by default
        # By negating the numbers, we effectively get a max heap
        heapq.heappush(self.small, -num)

        # Check if the root of the max heap (small) is greater than the root of the min heap (large)
        # If so, we need to rebalance the heaps
        if (self.small and self.large and -self.small[0] > self.large[0]):
            # Pop the root from the max heap (small)
            val = heapq.heappop(self.small)
            # Push the negated value to the min heap (large)
            heapq.heappush(self.large, -val)

        # Check if the size of the max heap (small) is more than the size of the min heap (large) + 1
        # If so, we need to rebalance the heaps
        if len(self.small) > len(self.large) + 1:
            # Pop the root from the max heap (small)
            val = heapq.heappop(self.small)
            # Push the negated value to the min heap (large)
            heapq.heappush(self.large, -val)

        # Check if the size of the min heap (large) is more than the size of the max heap (small) + 1
        # If so, we need to rebalance the heaps
        if len(self.large) > len(self.small) + 1:
            # Pop the root from the min heap (large)
            val = heapq.heappop(self.large)
            # Push the negated value to the max heap (small)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If the size of the max heap (small) is greater than the size of the min heap (large)
        if len(self.small) > len(self.large):
            # The median is the root of the max heap (small)
            return -self.small[0]
        # If the size of the min heap (large) is greater than the size of the max heap (small)
        if len(self.large) > len(self.small):
            # The median is the root of the min heap (large)
            return self.large[0]
        # If the sizes of both heaps are equal
        # The median is the average of the roots of both heaps
        return (-self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
