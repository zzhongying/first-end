from typing import List

class MaxQueue:

    def __init__(self):
        self.val = []
        self.max = []

    def max_value(self) -> int:
        return self.max[-1] if len(self.max) != 0  else -1

    def push_back(self, value: int) -> None:
        self.val.append(value)
        if len(self.max) == 0:
            self.max.append(value)
        elif (value >= self.max[-1]):  #由小至大递增
            self.max.append(value)

    def pop_front(self) -> int:
        if len(self.val) != 0 and len(self.max)!=0:
            if self.val[0] == self.max[-1]:
                self.val.pop(0)
                return self.max.pop()
            else:
                return self.val.pop(0)
        else:
            return -1
