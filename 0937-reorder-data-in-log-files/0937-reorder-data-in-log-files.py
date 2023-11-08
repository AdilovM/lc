class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_logs = []
        dig_logs = []
        for log in logs:
            split_log = log.split()
            dig_logs.append(log) if split_log[1].isdigit() else let_logs.append(split_log)
        let_logs.sort(key = lambda x: (x[1:], x[0]))
        print(let_logs)
        let_logs = [" ".join(log) for log in let_logs] 
        print(let_logs)
        return let_logs + dig_logs