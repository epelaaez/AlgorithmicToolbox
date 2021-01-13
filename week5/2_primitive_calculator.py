import sys

def optimal_sequence(n):
    sequences    = [float("inf")] * (n + 1)
    sequences[1] = [1]

    for i in range(2, n + 1):
        divide_2 = float("inf")
        divide_3 = float("inf")
        add_1    = float("inf")
        
        if i % 2 == 0:
            divide_2 = len(sequences[i // 2]) + 1
        if i % 3 == 0:
            divide_3 = len(sequences[i // 3]) + 1
        if i - 1 > 0:
            add_1 = len(sequences[i - 1]) + 1

        steps = min(divide_2, divide_3, add_1)

        sequence = []

        if steps == divide_2:
            for j in sequences[i // 2]:
                sequence.append(j)
        elif steps == divide_3:
            for k in sequences[i // 3]:
                sequence.append(k)
        else:
            for l in sequences[i - 1]:
                sequence.append(l)
        sequence.append(i)
        
        sequences[i] = sequence
        
    return sequences[n]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
