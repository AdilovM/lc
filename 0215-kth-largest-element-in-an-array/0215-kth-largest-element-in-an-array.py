class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        simpe way:
        1. order desc
        2. return kth element
        
        quickselect
        1. choose pivot index, usually last index. swap elements so left side of pivot is less than kth element
        and right side of pivot is greater than kth element
        2. if pivot == k return pivot
        3. if pivot < k, do quick select on right side, pivot = k - pivot and continue quickselect. 
        example: k = 5 but pivot = 2, new pivot = 5 -2 = 3
        4. if pivot > k, do quickselect on left side, we do search until pivot
        curr
        [3,2,1,5,6,4]
        p           
        """
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1
        
        remain = k
        # print(count)
        for idx in range(len(count)-1, -1, -1):
            remain -= count[idx]
            if remain <= 0:
                return idx + min_value # becase idx=num-min_value, then num=idx+min_value

        return -1
        