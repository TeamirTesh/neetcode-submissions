from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((timestamp, value))
            
    def get(self, key: str, timestamp: int) -> str:
        idx = self.search(key, timestamp)
        if idx is None or idx == -1:
            return ""

        return self.time[key][idx][1]

    def search(self, key: str, timestamp: int):
        if key not in self.time:
            return None

        l, r = 0, len(self.time[key]) - 1
        res = -1

        while l <= r:
            mid = (l + r) // 2
            if self.time[key][mid][0] == timestamp:
                return mid

            elif self.time[key][mid][0] < timestamp:
                l = mid + 1
                res = mid

            else:
                r = mid - 1
            
        return res