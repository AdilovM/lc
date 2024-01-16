class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        from collections import Counter

        def dfs(target):
            if not target: return 0
            if target in memo: return memo[target]

            res = float('inf')
            t_count = Counter(target)

            for s in stickers:
                # Skip this sticker if it does not contain the first character of target
                if target[0] not in s: continue

                # Create a new target string after using this sticker
                new_target = ''.join([c * (t_count[c] - s[c]) for c in t_count])

                # Recursive call
                tmp = dfs(new_target)
                if tmp != -1: res = min(res, 1 + tmp)

            memo[target] = -1 if res == float('inf') else res
            return memo[target]

        # Preprocess stickers
        stickers = [Counter(sticker) for sticker in stickers]

        memo = {}
        result = dfs(target)

        return -1 if result == float('inf') else result