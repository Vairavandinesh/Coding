class Solution:
    def minCostClimbingStairs(self, cost):
        #the goal is to find the minimum cost to reach the top of the array(getting out of it)
        #let the number of costs be n
        n=len(cost)
        #in tabulation(dp) we create an array and update the values to retrieve easily , so create an array with the length + 1
        dp=[0]*(n+1)
        #we know that the cost to reach the first 2 steps is zero , so the loop starts from 2
        for i in range(2,n+1):
            #the formula to find the minimum cost for each step in the dp array is minimum of (cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])
            dp[i]=min(cost[i-2]+dp[i-2],cost[i-1]+dp[i-1])
        return dp[n]
cost=[10,15,20]
sol=Solution()
print(sol.minCostClimbingStairs(cost))