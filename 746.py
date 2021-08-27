class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = len(cost)
        min_cost = []
        
        min_cost.append(cost[0])
        min_cost.append(cost[1])
        
        for i in range(2, L):
            min_cost.append(min(min_cost[i - 2], min_cost[i - 1]) + cost[i])
            
        return min(min_cost[-1], min_cost[-2])
