import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    for i in range(n):
        exp_max[i][i] = digits[i]
        exp_min[i][i] = digits[i]

    for s in range(0, n):
        for i in range(0, n - s - 1):
            j = i + s + 1
            min_value, max_value = min_max_value(i, j)
            exp_max[i][j] = max_value
            exp_min[i][j] = min_value

def min_max_value(i, j):
    min_value = float('inf')
    max_value = float('-inf')

    for k in range(i, j):
        a = evalt(exp_max[i][k], exp_max[k + 1][j], ops[k])
        b = evalt(exp_max[i][k], exp_min[k + 1][j], ops[k])
        c = evalt(exp_min[i][k], exp_max[k + 1][j], ops[k])
        d = evalt(exp_min[i][k], exp_min[k + 1][j], ops[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    return min_value, max_value


if __name__ == "__main__":
    dataset = input()
    digits = list(map(int, dataset[0::2]))
    n = len(digits)
    ops = list(dataset[1::2])
    exp_min = [[0 for x in range(n)] for y in range(n)]
    exp_max = [[0 for x in range(n)] for y in range(n)]
    get_maximum_value(dataset)
    print(exp_max[0][n - 1])