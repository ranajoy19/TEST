# Dynamic Programming ===>>>> <<=============


# 0 - 1 Knapsack Problem


# You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
# In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property).

# Example 1:

# Input:
# N = 3
# W = 4
# values[] = {1,2,3}
# weight[] = {4,5,1}
# Output: 3
# Explanation: Choose the last item that weighs 1 unit and holds a value of 3.


def knapSack(W, wt, val, N):
    dp = {}

    def sol(n, cap):
        if n == 0 or cap == 0:
            return 0
        elif (n, cap) in dp:
            return dp[(n, cap)]
        else:
            cwt = wt[n - 1]
            cv = val[n - 1]
            if cwt <= cap:
                r1 = cv + sol(n - 1, cap - cwt)
                r2 = sol(n - 1, cap)
                result = max(r1, r2)
            else:
                result = sol(n - 1, cap)
            dp[(n, cap)] = result
            return result

    return sol(N, W)


print(knapSack(4,[4,5,1],[1,2,3],3))