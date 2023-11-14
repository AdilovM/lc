class Solution:
    def countBits(self, n: int) -> List[int]:
        num_bits = [0] * (n + 1)
        for i in range(1, n + 1):
            num_bits[i] = num_bits[int(i/2)] + i%2
        return num_bits