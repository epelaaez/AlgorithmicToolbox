import sys

def fibonacci_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1

    for i in range(n + 2):
        a, b = b, a + b

    return (a - 1) % 10

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum(n % 60))