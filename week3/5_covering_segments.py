import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments = sorted(segments, key = lambda s: s.start) # sort segments by starting point

    points = []
    common_points = []

    while len(segments) > 0:
        reached_sequences = []

        shortest_segment = segments[0]
        for segment in segments:
            if segment.start != segments[0].start:
                break
            if segment.end - segment.start <= shortest_segment.end - shortest_segment.start:
                shortest_segment = segment
        common_points = [*range(shortest_segment.start, shortest_segment.end + 1)]

        for i in range(len(segments)):
            if segments[i].start <= common_points[-1]:
                reached_sequences.append(segments[i])
                if segments[i].end >= common_points[-1]:
                    common_points = [*range(segments[i].start, segments[0].end + 1)]
                else:
                    common_points = [*range(segments[i].start, segments[i].end + 1)]
            else:
                break
            
        points.append(common_points[-1])
        for point in reached_sequences:
            segments.remove(point)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)