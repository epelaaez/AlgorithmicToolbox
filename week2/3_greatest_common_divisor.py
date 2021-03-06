import sys

def greatest_common_divisor(a, b):
    gcd = -1
    
    if a < 0 or b < 0:
        return gcd
    elif a == 0:
        return b
    elif b == 0:
        return a

    a_prime = a % b

    return greatest_common_divisor(b, a_prime)

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(greatest_common_divisor(a, b))