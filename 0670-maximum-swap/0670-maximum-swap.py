class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))  # Convert the number to a list of its digits
        last_idx = {int(x): i for i, x in enumerate(num_list)}  # Store the last index of each digit

        for i, digit in enumerate(num_list):
            for d in range(9, int(digit), -1):  # Check for a larger digit to swap with
                if last_idx.get(d, -1) > i:  # If a larger digit is found and it's positioned after the current digit
                    num_list[i], num_list[last_idx[d]] = num_list[last_idx[d]], num_list[i]  # Swap the digits
                    return int(''.join(num_list))  # Return the new number after the swap

        return num  