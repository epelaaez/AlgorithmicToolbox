import sys
import math

def minimum_distance(x, y):
    points = []
    for i, j in enumerate(x):
        points.append((j, y[i]))

    # Sort points by x and y coordinate
    points.sort(key=lambda x: (x[0], x[1]))

    return find_min_distance(points)

def find_min_distance(p):
    if len(p) == 2:
        return distance(p[1], p[0])
    elif len(p) == 1:
        return float('inf') # To not count distance between the same point as the minimum one

    mid = int(len(p) / 2)

    left_min  = find_min_distance(p[0:mid])
    right_min = find_min_distance(p[mid:])

    d_1 = min(left_min, right_min)
    d_2 = find_min_between_sections(p[0:mid], p[mid:], d_1, p[mid])

    return min(d_1, d_2)

def find_min_between_sections(a, b, d, mid):
    possible_points = []
    d_2 = d

    for point in a:
        if distance(point, (mid[0], point[1])) > d:
            pass
        else:
            possible_points.append(point)

    for point in b:
        if distance(point, (mid[0], point[1])) < d:
            pass
        else:
            possible_points.append(point)

    possible_points.append(mid)

    # Sort points by their y coordinate
    possible_points.sort(key=lambda x: x[1])
    for i, point_1 in enumerate(possible_points):
        for j, point_2 in enumerate(possible_points):
            if abs(i - j) <= 7 and i != j:
                d_2 = min(d_2, distance(point_1, point_2))
    
    return min(d, d_2)

def distance(point1, point2):
    """
    Helper function to find distance between two points
    """
    x = math.pow(point1[0] - point2[0], 2)
    y = math.pow(point1[1] - point2[1], 2)
    return math.sqrt(x + y)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
