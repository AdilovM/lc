class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log = []
        digit_log = []

        for i in logs:
            if i.split()[1].isdigit():
                digit_log.append(i)
            else:
                letter_log.append(i)

        letter_log.sort(key=lambda a : (a.split()[1:], a.split()[0]))

        return letter_log + digit_log