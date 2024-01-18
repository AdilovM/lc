class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # Case where current asteroid moves to the right or no collision is possible
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                # Check for collisions
                while stack and stack[-1] > 0:
                    if stack[-1] < -asteroid:
                        stack.pop()
                        continue
                    elif stack[-1] == -asteroid:
                        stack.pop()
                    break
                else:
                    stack.append(asteroid)

        return stack