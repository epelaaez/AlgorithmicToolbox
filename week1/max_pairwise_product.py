def max_pairwise_product(numbers):
    max_num_1 = -1;
    max_num_2 = -1;

    for num in numbers:
        if (num > max_num_1):
            max_num_2 = max_num_1
            max_num_1 = num
        elif (num > max_num_2):
            max_num_2 = num

    return max_num_1 * max_num_2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
