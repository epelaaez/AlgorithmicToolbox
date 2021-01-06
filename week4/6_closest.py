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
            if abs(point[0] - mid[0]) < d:
                point_a = [i, point]
                break
            else:
                a.pop(i)
        
        for i, point in enumerate(b):
            if abs(point[0] - mid[0]) < d:
                point_b = [i, point]
                break
            else:
                b.pop(i)                

        if point_a is None and point_b is None:
            break
        elif point_a is None and point_b is not None:
            possible_points.append(point_b[1])
            b.pop(point_b[0])
        elif point_b is None and point_a is not None:
            possible_points.append(point_a[1])
            a.pop(point_a[0])
        else:
            if point_b[1] < point_a[1]:
                possible_points.append(point_b[1])        
                b.pop(point_b[0])
            else:
                possible_points.append(point_a[1])
                a.pop(point_a[0])

    if len(a) != 0:
        for point in a:
            if abs(point[0] - mid[0]) < d:
                possible_points.append(point)
            else:
                break
    elif len(b) != 0:
        for point in b:
            if abs(point[0] - mid[0]) < d:
                possible_points.append(point)
            else:
                break
    
    for i, point in enumerate(possible_points):
        upper = min(i + 7, len(possible_points) - 1)
        for j in range(i + 1, upper + 1):
            d_2 = min(d_2, distance(point, possible_points[j]))
    
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
