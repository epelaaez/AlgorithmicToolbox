import sys

def optimal_summands(n):
    summands = []
    total = 0
    current_number = 0    

    while total <= n:
        if total + (current_number + 1) <= n:
            current_number += 1
            summands.append(current_number)
            total += current_number
        else:
            summands[-1] = (n + summands[-1]) - total
            break
    
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
