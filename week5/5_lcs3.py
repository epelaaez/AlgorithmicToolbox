import sys

def lcs3(a, b, c):
    solution = [[[0] * len(c) for i in range(len(b))] for j in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                if a[i] == b[j] == c[k]:
                    if i - 1 >= 0 and j - 1 >= 0 and k - 1 >= 0:
                        solution[i][j][k] = solution[i - 1][j - 1][k - 1] + 1
                    else:
                        solution[i][j][k] += 1
                else:
                    if i - 1 >= 0 and j - 1 >= 0 and k - 1 >= 0:
                        solution[i][j][k] = max(solution[i - 1][j][k], solution[i][j - 1][k], solution[i][j][k - 1])
                    elif i - 1 < 0:
                        solution[i][j][k] = max(solution[i][j - 1][k], solution[i][j][k - 1])
                    elif j - 1 < 0:
                        solution[i][j][k] = max(solution[i - 1][j][k], solution[i][j][k - 1])
                    else:
                        solution[i][j][k] = max(solution[i - 1][j][k], solution[i][j - 1][k])

    return solution[len(a) - 1][len(b) - 1][len(c) - 1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
