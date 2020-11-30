import sys

def fibonacci_huge(n, m):
    period = find_period(m)
    index = n % len(period)
    return period[index]

def find_period(m):
    period = []
    iteration = 0

    while(True):
        period.append(fibonacci_number(iteration) % m)
        if len(period) >= 4 and period[0] == period[-2] and period[1] == period[-1]:
            period = period[:len(period) - 2]
            break
        iteration += 1

    return period

def fibonacci_number(n_number):
    if n_number <= 1:
        return n_number
    
    last_2 = 0
    last_1 = 1
    answer = 0

    for _ in range(2, n_number + 1):
        answer = last_2 + last_1
        last_2 = last_1
        last_1 = answer
        
    return answer

if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(fibonacci_huge(n, m))
