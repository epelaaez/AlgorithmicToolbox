import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    
    # Create a number line containing elements of the form [number, type]
    # Number can take on any number and type will be the letter 'l', 'r' 'p' (indicating leftmost of a segment, rightmost of a segment or point)
    number_line = []

    # Add leftmost points of all segments
    for l in starts:
        number_line.append([l, 'l'])
    
    # Add rightmost points of all segments
    for r in ends:
        number_line.append([r, 'r'])
    
    # Add points
    for i, p in enumerate(points):
        number_line.append([p, 'p', i])

    # Sort number line
    number_line.sort(key=lambda x: (x[0], x[1]))
    
    # Keep count of the number of segments currently inside of
    segments = 0
    for number in number_line:
        if number[1] == 'l':
            segments += 1
        elif number[1] == 'r':
            segments -= 1
        else:
            cnt[number[2]] += segments

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    # cnt = naive_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
