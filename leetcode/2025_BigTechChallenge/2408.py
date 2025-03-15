from collections import defaultdict
from typing import List


class Table:
    def __init__(self, name: str, cols: int):
        self.name = name
        self.cols = cols
        self.rows = defaultdict(list)
        self.id = 0

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = defaultdict(Table)
        n = len(names)
        for i in range(n):
            table = Table(names[i], columns[i])
            self.tables[names[i]] = table

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tables:
            return False
        if len(row) != self.tables[name].cols:
            return False
        self.tables[name].id += 1
        self.tables[name].rows[self.tables[name].id] = row
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.tables or rowId not in self.tables[name].rows:
            return
        del self.tables[name].rows[rowId]
        return

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables or rowId not in self.tables[name].rows or columnId <= 0 or columnId > len(self.tables[name].rows[rowId]):
            return "<null>"
        return self.tables[name].rows[rowId][columnId - 1]

    def exp(self, name: str) -> List[str]:
        if name not in self.tables:
            return []
        ans = []
        for id, content in self.tables[name].rows.items():
            l = []
            l.append(str(id))
            l += content
            ans.append(",".join(l))
        return ans