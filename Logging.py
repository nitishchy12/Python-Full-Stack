from collections import defaultdict, deque
import functools
import json  # keep this from your local changes

logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]

# decorator
def parse_log(add_log):
    def wrapper(log):
        arr = log.split(" ", 3)
        timestamp = arr[0].strip("[]")
        level = arr[1]
        user = arr[2].strip(":")
        message = arr[3]
        log_dict = {
            "TimeStamp": timestamp,
            "level": level,
            "user": user,
            "message": message
        }
        result = add_log(log_dict)
        print("converted string log to dict")
        return result
    return wrapper


# logging function
userDict = defaultdict(list)
levelDict = defaultdict(int)
recentLogs = deque(maxlen=3)
logs_dict = {}


@parse_log
def add_log(log):
    user = log["user"]
    level = log["level"]
    userDict[user].append(log)
    levelDict[level] += 1
    recentLogs.append(log)


for i in logs:
    add_log(i)

# File writing and reading logic from your local update
with open("logs.txt", "w") as file_:
    for log in logs:
        file_.write(log + "\n")

with open("logs.txt", "r") as file_:
    for line in file_:
        add_log(line.strip())

with open("file2.txt", "w") as file_:
    file_.write("Hello World3\n")

with open("file2.txt", "a") as file_:
    file_.write("Hello world4\n")

with open("sample.json", "w") as file_:
    json.dump(userDict, file_, indent=4)  # i should declare json file (H.W)

print(userDict)
print(levelDict)
print(recentLogs)
