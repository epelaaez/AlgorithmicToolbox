def get_fibonacci_last_digit_naive(n_number):
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
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
