class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        pointer1, pointer2 = 0, 0
        result = []

        while pointer1 < len(encoded1) and pointer2 < len(encoded2):
            # Get the value and frequency from both encoded arrays
            val1, freq1 = encoded1[pointer1]
            val2, freq2 = encoded2[pointer2]

            # Calculate the product of values and the minimum frequency
            product = val1 * val2
            min_freq = min(freq1, freq2)

            # Update the frequencies in the original arrays
            encoded1[pointer1][1] -= min_freq
            encoded2[pointer2][1] -= min_freq

            # Move pointers if the frequency becomes zero
            if encoded1[pointer1][1] == 0:
                pointer1 += 1
            if encoded2[pointer2][1] == 0:
                pointer2 += 1

            # Append the product and its frequency to the result
            if not result or result[-1][0] != product:
                result.append([product, min_freq])
            else:
                result[-1][1] += min_freq

        return result
        