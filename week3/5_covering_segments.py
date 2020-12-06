import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    smallest_pair, smallest_length = [], float("inf")
    reached = []

    for s in segments:
        if s.end - s.start <= smallest_length:
            smallest_length = s.end - s.start
            smallest_pair = s
            reached.append(s)
            segments.remove(s)
    
    for s in segments:
        if s.start <= smallest_pair.end and s.end >= smallest_pair.start:
            reached.append(s)
            if s.start not in points:
                points.append(s.start) 
            segments.remove(s)

    if len(segments) == 0:
        return points

    return points + optimal_points(segments)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)