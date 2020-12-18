import sys

def binary_search(a, x):
    low, high = 0, len(a)
    while True:
        if high < low:
            return -1
        mid = low + ((high - low) // 2)
        if mid < 0 or mid >= len(a):
            return -1
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            high = mid - 1 
            pass
        else:
            low = mid + 1
            pass

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
