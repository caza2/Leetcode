from collections import defaultdict

class TimeMap:

    def __init__(self) -> None:
        self.store: dict[str, list[list[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        data: list[list] = self.store[key]
        if not data:
            return ""
        if len(data) == 1:
            return data[0][1] if timestamp >= data[0][0] else ""
        left, right = 0, len(data) - 1
        while left <= right:
            middle = (left+right)//2
            if data[middle][0] == timestamp:
                return data[middle][1]
            elif data[middle][0] < timestamp:
                left = middle + 1
                if left >= len(data) or data[left][0] > timestamp:
                    return data[middle][1]
            else:
                right = middle - 1
                if right < 0:
                    return ""
                if data[right][0] < timestamp:
                    return data[right][1]
        return ""