import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
   
    for _ in range(len(weights)):
        if capacity == 0:
            return value
        index = select_item(weights, values)
        amount = weights[index] if weights[index] < capacity else capacity
        value += amount * (values[index] / weights[index])
        weights[index] -= amount
        capacity -= amount

    return value

def select_item(weights, values):
    best = float("-inf")
    index = 0

    for i in range(len(weights)):
        if weights[i] != 0 and (values[i] / weights[i]) >= best:
            best = values[i] / weights[i]
            index = i
    return index

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
