import sys

def lcs2(a, b):
    if min(len(a), len(b)) == len(a):
        a, b = b, a

    pointer = 0
    while len(b) != 0 and len(a) != 0:
        if pointer >= len(a):
                break
        if a[pointer] == b[0]:
            pointer += 1
            b.pop(0)
        else:
            a.pop(pointer)
            
    return len(a)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
