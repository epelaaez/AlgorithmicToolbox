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

    while len(a) != 0 and len(b) != 0:
        point_a = None
        point_b = None

        for i, point in enumerate(a):
            if distance(point, (mid[0], point[1])) < d:
                point_a = point
                a.pop(i)
                break
            else:
                a.pop(i)
        
        for i, point in enumerate(b):
            if distance(point, (mid[0], point[1])) < d:
                point_b = point
                b.pop(i)
                break
            else:
                b.pop(i)

        if point_a is None and point_b is None:
            break
        elif point_a is None and point_b is not None:
            possible_points.append(point_b)
        elif point_b is None and point_a is not None:
            possible_points.append(point_a)
        else:
            if point_a[1] > point_b[1]:
                possible_points.append(point_b)        
                possible_points.append(point_a)
            else:
                possible_points.append(point_a)
                possible_points.append(point_b)
    
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
