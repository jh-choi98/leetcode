from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterlogs = []
        digitlogs = []
        for log in logs:
            log_list = log.split()
            if log_list[1].isdigit():
                digitlogs.append(log)
            else:
                letterlogs.append(log)
        letterlogs = sorted(letterlogs, key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))
        return letterlogs + digitlogs
