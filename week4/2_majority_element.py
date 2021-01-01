import sys

def get_majority_element(a, left, right):
    # Solved using non divide and conquer approach

    counts = dict()   

    for element in a:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    
    for element, count in counts.items():
        if count > (right / 2):
            return element

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
