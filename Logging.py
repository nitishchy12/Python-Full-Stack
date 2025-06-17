from collections import deque, defaultdict
import re
from functools import wraps

# decorator 
def parse_log(add_log):
    def wrapper(logs):
        match = re.match(r"\[(.*?)\] (\w+) (\w+): (.*)", line)
        if not match:
            return  
        timestamp, level, user, message = match.groups()
        log_dict = {
            "timestamp": timestamp,
            "level": level,
            "user": user,
            "message": message
        }
        return add_log(self, log_dict)
    return wrapper

class LogSystem:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recent_logs = deque(maxlen=capacity)
        self.user_logs = defaultdict(list)
        self.level_counts = defaultdict(int)

    def add_log(self, line: str) -> None:
        match = re.match(r"\[(.*?)\] (\w+) (\w+): (.*)", line)
        if not match:
            return
        timestamp, level, user, message = match.groups()
        log_dict = {
            "timestamp": timestamp,
            "level": level,
            "user": user,
            "message": message
        }


        self.recent_logs.append(log_dict)
        self.user_logs[user].append(log_dict)
        self.level_counts[level] += 1

    def get_user_logs(self, user_id: str) -> list[dict]:
        return list(self.user_logs.get(user_id, []))

    def count_levels(self) -> dict[str, int]:
        return dict(self.level_counts)

    def filter_logs(self, keyword: str) -> list[dict]:
        keyword_lower = keyword.lower()
        return [
            log for log in self.recent_logs
            if keyword_lower in log["message"].lower()
        ]

    def get_recent_logs(self) -> list[dict]:
        return list(self.recent_logs)

logs = [
    "[2025-06-16T10:00:00] INFO Sushant: Started process",
    "[2025-06-16T10:00:01] ERROR Sushant: Failed to connect",
    "[2025-06-16T10:00:02] INFO Namit: Login successful",
    "[2025-06-16T10:00:03] WARN Anurag: Low memory",
    "[2025-06-16T10:00:04] ERROR Namit: Timeout occurred",
    "[2025-06-16T10:00:05] INFO Sushant: Retrying connection"
]

logsys = LogSystem(capacity=5)

for log_line in logs:
    logsys.add_log(log_line)


print(logsys.get_user_logs("Sushant"))
print(logsys.count_levels())
print(logsys.filter_logs("connect"))
print(logsys.get_recent_logs())
