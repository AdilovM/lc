class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_count = Counter(ages)
        request_count = 0

        for age_A in age_count:
            for age_B in age_count:
                if age_B <= 0.5 * age_A + 7 or age_B > age_A or (age_B > 100 and age_A < 100):
                    continue
                request_count += age_count[age_A] * (age_count[age_B] - (age_A == age_B))

        return request_count