# Uses python3
import sys

def fibonacci_sum(n):
    answer = 0
    
    for i in range(n + 1):
        answer += fibonacci_last_digit(i)
    
    while(answer >= 10):
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
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_naive(n))