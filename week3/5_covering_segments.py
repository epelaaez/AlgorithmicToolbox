import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments = sorted(segments, key = lambda s: s.end) # sort segments by point point
    current_point = segments[0].end
    points = [current_point] 

    for segment in segments:
        if current_point < segment.start:
            current_point = segment.end
            points.append(current_point)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)