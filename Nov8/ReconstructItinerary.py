# 332. Reconstruct Itinerary

from typing import List
from collections import defaultdict

class Solution:

    def __init__(self):
        self.list = []
        self.ticket_dict = defaultdict(list)

    # exceed time limit
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for t in tickets:
            a = t[0]
            b = t[1]
            self.ticket_dict[a].append(b)
        
        for target in self.ticket_dict:
            self.ticket_dict[target].sort()
        
        self.list.append("JFK")
        self.backtrack(len(tickets), "JFK", "JFK")
        return self.list

    def backtrack(self, n, start, cur):
        if len(self.list) == n+1:
            return True

        for i, nxt in enumerate(self.ticket_dict[cur]): 
            self.list.append(nxt)
            self.ticket_dict[cur].pop(i)
            if self.backtrack(n, start, nxt):
                return True
            self.ticket_dict[cur].insert(i, nxt)
            self.list.pop()
        return False


    # exceed time limit
    def findItinerary_2(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        used = [0] * len(tickets)
        path = ['JFK']
        result = []
        self.backtrack_2(tickets, used, path, 'JFK', result)
        return result[0]
    

    def backtrack_2(self, tickets, used, path, cur, result):
        if len(path) == len(tickets) + 1:
            result.append(path[:])
            return True
        for i in range(len(tickets)):
            if tickets[i][0] == cur and used[i] == 0:
                path.append(tickets[i][1])
                used[i] = 1
                if self.backtrack_2(tickets, used, path, tickets[i][1], result):
                    return True
                path.pop()
                used[i] = 0

    # 逆序
    def findItinerary_3(self, tickets: List[List[str]]) -> List[str]:
        targets = defaultdict(list)
        for ticket in tickets:
            targets[ticket[0]].append(ticket[1])
        for key in targets:
            targets[key].sort(reverse = True)
        
        result = []
        self.backtracking_3('JFK', result, targets)
        return result[::-1]
    
    def backtracking_3(self, airport, result, targets):
        while targets[airport]:
            nxt = targets[airport].pop() 
            self.backtracking_3(nxt, result, targets)
        result.append(airport)