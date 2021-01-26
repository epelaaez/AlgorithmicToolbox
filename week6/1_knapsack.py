import sys

def optimal_weight(W, w):
    solution = [[0] * len(w) for _ in range(W + 1)]

    for i in range(len(w)):
        for j in range(W + 1):
            solution[j][i] = solution[j][i - 1]
            if w[i] <= j:
                value = solution[j - w[i]][i - 1] + w[i]
                if solution[j][i] < value:
                    solution[j][i] = value
    
    return solution[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
