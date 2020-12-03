import sys

def get_change(m):
    total = 0
    coins = [10, 5, 1]
    i = 0

    while m != 0 and i != len(coins):
        if m >= coins[i]:
            n_coins = m // coins[i]
            total += n_coins
            m -= coins[i] * n_coins
        else:
            i += 1
    return total

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
