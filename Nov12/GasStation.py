# 134. Gas Station

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr = []
        n = len(gas)
        tot = 0
        for i in range(n):
            arr.append(gas[i] - cost[i])
            tot += arr[i]
        if tot < 0:
            return -1
        
        for i in range(n):

            if arr[i] < 0:
                continue
            if i > 0 and arr[i] == arr[i-1]:
                continue
            bal = 0
            for j in range(i, n):
                bal += arr[j]
                if bal < 0:
                    break
                if j == n - 1:
                    return i
        return -1

    def canCompleteCircuit_eg(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = 0
        total_cost = 0
        startidx = 0
        tank = 0
        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                startidx = i+1
                tank = 0
        if total_cost > total_gas:
            return -1
        return startidx