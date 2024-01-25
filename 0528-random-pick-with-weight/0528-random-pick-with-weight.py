class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []  # Initialize an empty list to store prefix sums
        prefix_sum = 0  # Initialize prefix_sum to 0
        for weight in w:  # Iterate over each weight in the input list 'w'
            prefix_sum += weight  # Add the current weight to the prefix_sum
            self.prefix_sums.append(prefix_sum)  # Append the updated prefix_sum to the list
        self.total_sum = prefix_sum  # Store the total sum of weights
        self.pickIndex()  # Call the pickIndex method

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()  # Generate a random target value
        low, high = 0, len(self.prefix_sums)  # Initialize binary search bounds
        while low < high:  # Binary search loop
            mid = (low + high) // 2  # Find the middle index
            if self.prefix_sums[mid] < target:  # Compare middle value with target
                low = mid + 1  # Adjust the lower bound
            else:
                high = mid  # Adjust the upper bound
        return low  # Return the final low value as the index



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()