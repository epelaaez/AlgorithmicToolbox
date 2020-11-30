import sys

def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    
    n %= 60
    answer = fibonacci_last_digit(n) * fibonacci_last_digit(n + 1)
    while (answer >= 10):
        answer %= 10

    return answer

def fibonacci_last_digit(n_number):
    if n_number <= 1:
        return n_number
    
    last_2 = 0
    last_1 = 1
    answer = 0

    for _ in range(2, n_number + 1):
        answer = (last_2 + last_1)  % 10
        last_2 = last_1
        last_1 = answer
        
    return answer

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(fibonacci_sum_squares(n))
