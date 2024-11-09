# Дан массив транзакций transactions, где transactions[i] = [fromi, toi, amounti] указывает на то, что человек с ID = fromi дал сумму amounti долларов человеку с ID = toi.
# Верните минимальное количество транзакций, необходимых для урегулирования долгов.

"""
Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
"""

from typing import List
from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
            credit_map = defaultdict(int)
            for t in transactions:
                # Создать хеш-таблицу для хранения чистого баланса каждого человека.
                credit_map[t[0]] += t[2]
                credit_map[t[1]] -= t[2]

            # Собрать все ненулевые чистые балансы в массив balance_list.
            credit_list = [amount for amount in credit_map.values() if amount != 0]
            n = len(credit_list)

            def dfs(cur):
                while cur < n and credit_list[cur] == 0:
                    cur += 1
                if cur == n:
                    return 0

                cost = float('inf')
                for nxt in range(cur + 1, n):
                    if credit_list[nxt] * credit_list[cur] < 0:
                        credit_list[nxt] += credit_list[cur]
                        cost = min(cost, 1 + dfs(cur +1 ))
                        credit_list[nxt] -= credit_list[cur]
                return cost

            return dfs(0)

if __name__ == "__main__":
    example = Solution()
    result = example.minTransfers(transactions = [[0,1,10],[2,0,5]])
    print(result)

