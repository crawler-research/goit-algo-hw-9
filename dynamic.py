def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    result = {}
    i = amount
    while i > 0:
        for coin in coins:
            if dp[i] == dp[i - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                i -= coin
                break

    return result

print(123, find_min_coins(123))  # {50: 2, 10: 2, 2: 1, 1: 1}
