class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_times = [0] * n
        stack = []  # Stack to keep track of function calls
        prev_time = 0  # Previous timestamp

        for log in logs:
            func_id, typ, time = log.split(':')
            func_id, time = int(func_id), int(time)

            if typ == 'start':
                if stack:
                    # Update the time of the function at the stack's top
                    exclusive_times[stack[-1]] += time - prev_time
                stack.append(func_id)
                prev_time = time
            else:
                # End of function call
                exclusive_times[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return exclusive_times