import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments = sorted(segments, key = lambda s: s.start) # sort segments by starting point

    points = []
    common_points = []

    while len(segments) != 0:
        reached_points = []
        common_points = [*range(segments[0].start, segments[0].end + 1)]
        for i in range(len(segments)):
            if segments[i].start <= segments[0].end:
                reached_points.append(segments[i])
                if segments[i].end >= segments[0].end:
                    common_points = [*range(segments[i].start, segments[0].end + 1)]
                else:
                    common_points = [*range(segments[i].start, segments[i].end + 1)]
            else:
                break

        points.append(common_points[0])
        for point in reached_points:
            segments.remove(point)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)