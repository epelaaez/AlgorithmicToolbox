import sys

def largest_number(a):
    res = ""

    while len(a) > 0:
        max_number = float("-inf")
        for number in a:
            if greater_or_equal(number, max_number):
                max_number = number
        res += str(max_number)
        a.remove(max_number)

    return res

def greater_or_equal(number, max_number):
    if max_number == float("-inf"):
        return True
    return int(str(number) + str(max_number)) >= int(str(max_number) + str(number))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
