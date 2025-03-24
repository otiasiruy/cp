from collections import defaultdict
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.acc = defaultdict(int)
        for i in range(len(balance)):
            self.acc[i + 1] = balance[i]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in self.acc or account2 not in self.acc:
            return False
        if self.acc[account1] < money:
            return False
        self.acc[account1] -= money
        self.acc[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account not in self.acc:
            return False
        self.acc[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.acc or self.acc[account] < money:
            return False
        self.acc[account] -= money
        return True

