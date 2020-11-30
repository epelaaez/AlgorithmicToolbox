import sys

def fibonacci_partial_sum(from_, to):
    answer = 0
    period = find_period(10)
    from_ = from_ % len(period)
    to = from_ + (to - from_) % len(period) # makes sure difference between to and from_ remains the same after doing % len(period)

    for i in range(from_, to + 1):
        index = i % len(period)
        answer += period[index]
    
    while(answer >= 10):
        answer %= 10

    return answer

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
    input = sys.stdin.readline()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))