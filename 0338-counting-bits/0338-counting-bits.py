class Solution:
    def countBits(self, n: int) -> List[int]:
        # n+1 as we are going to count from 0 to n
        num_bits = [0] * (n + 1)
        # num_bits[0] will be 0 because 0 has count of set bit is 0
        # we can compute current set bit count using previous count
        # as n/2 in O(1) time
        # i%2 will be 0 for even number ans 1 for odd number
        for i in range(1, n + 1):
            num_bits[i] = num_bits[int(i//2)] + i%2
        return num_bits