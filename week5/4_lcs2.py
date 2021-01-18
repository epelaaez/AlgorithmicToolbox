import sys

def lcs2(a, b):
    solution = [[0] * len(b) for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if i - 1 >= 0 and j - 1 >= 0:
                    solution[i][j] = solution[i - 1][j - 1] + 1
                else:
                    solution[i][j] = 1
            else:
                if i - 1 >= 0 and j - 1 >= 0:
                    solution[i][j] = max(solution[i - 1][j], solution[i][j - 1])
                elif i - 1 < 0:
                    solution[i][j] = solution[i][j - 1]
                else:
                    solution[i][j] = solution[i - 1][j]

    return solution[len(a) - 1][len(b) - 1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
