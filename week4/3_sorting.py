import sys
import random

def partition3(a, l, r):
    x = a[l] # Pivot
    j = l

    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]

    m1, m2 = j, j # Case where there is only one element equal to the pivot (itself)

    while m1 > l and a[m1] == x:
        m1 -= 1

    while m2 < r and a[m2] == x:
        m2 += 1

    return m1 + 1, m2 - 1

def partition2(a, l, r):
    x = a[l] # Pivot
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    # m = partition2(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)

def stress_test(l, r):
    while True:
        a = []
        for _ in range(l):
            k = random.randint(0, r)
            a.append(k)
        a_copy = a.copy()
        randomized_quick_sort(a, 0, l - 1)
        if (a != sorted(a)):
            print("Incorrect")
            print(a_copy, a)
            return
        else:
            print("Correct")
            print(a_copy, a)

if __name__ == '__main__':
    # stress_test(1000, 500)
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
