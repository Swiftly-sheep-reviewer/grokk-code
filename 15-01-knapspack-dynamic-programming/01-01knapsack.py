"""
bottom up dynamic programming

for each item at index i and capacity c, we have 2 options
1. exclude the item at index i. we will take whatever profit we get from the
    sub-array excluding this item => dp[i-1][c]
2. Include the item at index i if its weight is not more than the capacity.
    We include its profit plus whatever we get from the remaining capacity and
    from remaining items. => profit[i] + dp[i-1][c-weight[i]]

Finally, our optimal solution will be maximum of the above 2 values.
dp[i][c] = max(dp[i-1][c], profit[i] + dp[i-1][c-weight[i]])
"""


def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [[0 for _ in range(capacity+1)] for _ in range(n)]
    # populate the capacity = 0 columns, with 0 capacity we have 0 profit
    for i in range(n):
        dp[i][0] = 0
    # if we have only one weight, we will take it if it is not more than the
    # capacity
    for c in range(capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            # exclude the item
            profit2 = dp[i-1][c]
            # take maximum
            dp[i][c] = max(profit1, profit2)
    # maxinum profit will be at the bottom-right corner.
    return dp[n-1][capacity]


def main():
    print(solve_knapsack(profits=[1, 6, 10, 16], weights=[1, 2, 3, 5], capacity=5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


if __name__ == "__main__":
    main()
