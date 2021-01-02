# Good video on the topic: https://www.youtube.com/watch?v=7_AJfusC6UQ&index=14&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V

import sys

def get_number_of_inversions(a):
    solution = merge_sort(a) # Sorted array will be returned in reverse, but we only care about the count of inverse in this problem
    return solution[0]

def merge_sort(a):
    if len(a) == 1:
        return [0, a]

    mid = int(len(a) / 2)

    ordered_left  = merge_sort(a[0:mid])
    ordered_right = merge_sort(a[mid:])

    return merge(ordered_left, ordered_right)

def merge(left, right):
    count = left[0] + right[0]
    left_array  = left[1]
    right_array = right[1]
    
    merged_ordered = []
    while len(left_array) != 0 and len(right_array) != 0:
        if left_array[0] > right_array[0]:
            merged_ordered.append(left_array[0])
            count += len(right_array)
            left_array.pop(0)
        else:
            merged_ordered.append(right_array[0])
            right_array.pop(0)

    # The loop will sometimes end with remaining elements either on the left or right array, they are added to the merged array after in order
    merged_ordered += left_array
    merged_ordered += right_array

    return [count, merged_ordered]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a))