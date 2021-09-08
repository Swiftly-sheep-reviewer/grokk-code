def solve_knapsack(profits, weights, capacity):
    # TODO: Write your code here
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [[0 for _ in range(capacity+1)] for _ in range(n)]

    # create capacity=0 column
    for i in range(n):
        dp[i][0] = 0
    # take in the first weight if it is less than capacity
    for c in range(capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    # process all sub-arrays for all capacity
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)

    return dp[n-1][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
