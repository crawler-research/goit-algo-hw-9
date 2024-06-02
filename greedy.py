def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        amount -= coin * count
        if count != 0:
            result[coin] = count

    return result

print(123, find_coins_greedy(123))  # {50: 2, 10: 2, 2: 1, 1: 1}