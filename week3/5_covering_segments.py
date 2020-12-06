import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments = sorted(segments, key = lambda s: s.start) # sort segments by starting point
    points = []

    while len(segments) > 0:
        reached_segments = []
        shortest_segment = segments[0]

        for segment in segments:
            if segment.start != segments[0].start:
                break
            if segment.end - segment.start <= shortest_segment.end - shortest_segment.start:
                shortest_segment = segment
        print(shortest_segment)
        for segment in segments:
            if segment.start <= shortest_segment.end:
                reached_segments.append(segment)
 
        common_points = [*range(reached_segments[0].start, reached_segments[0].end + 1)]
        for segment in reached_segments:
            common_points = [point for point in [x for x in range(segment.start, segment.end + 1)] 
                            if point in common_points]

        print(common_points, reached_segments)
        points.append(common_points[0])
        for point in reached_segments:
            segments.remove(point)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)