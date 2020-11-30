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
    input_n = int(input())
    print(fibonacci_number(input_n))