class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        counting = 0 
        from collections import Counter
        nums1_dict = Counter(nums1)
        nums2_dict = Counter(nums2)

        
        for i in range(0,len(nums1)):
            if nums1[i] in nums2_dict:
                counting +=1 
            else:
                pass
        answer.append(counting)
        counting = 0
        for j in range(0,len(nums2)):
            if nums2[j] in nums1_dict:
                counting +=1 
            else:
                pass 
        answer.append(counting)
        return answer